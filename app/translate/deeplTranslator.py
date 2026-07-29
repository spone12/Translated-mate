# DeepL translate
import datetime
import json
import random
import re
import time
from requests import Session
from requests.exceptions import RequestException

from .abstractTranslator import AbstractTranslator
from app.enums.Translate.translators import Translators
from app.enums.Translate.translatorsLimit import TranslatorsLimit


class DeeplTranslator(AbstractTranslator):
    """DeepL translator based on the internal JSON-RPC endpoint"""

    _baseUrl = "https://www2.deepl.com/jsonrpc"
    _DeepLId = 0
    _regex = r"(\S.+?([.!?♪。]|$))(?=\s+|$)"
    _requestTimeout = (5, 30)

    def translate(self, text: str, targetLang: str, sourceLang: str = "auto") -> str:
        """Translate text and repeat the request once if DeepL returns no result"""

        if sourceLang.lower() == targetLang.lower():
            return text

        if getattr(self, "_session", None) is None:
            self.generateDeeplId()
            self._createDeeplSession()

        result = self.requestTranslation(
            self.baseUrl,
            text,
            targetLang,
            sourceLang,
        )

        if result:
            return result

        # HTTP client
        self._createDeeplSession()
        self.generateDeeplId()

        result = self.requestTranslation(
            self.baseUrl,
            text,
            targetLang,
            sourceLang,
        )

        if not result:
            self._session = None

        return result

    def generateDeeplId(self) -> None:
        """Generate the initial JSON-RPC request ID"""

        baseIdMult = 10_000
        millisecondsSinceMidnight = int(
            (
                datetime.datetime.now()
                - datetime.datetime.combine(datetime.date.today(), datetime.time())
            ).total_seconds()
            * 1000
        )
        randomGenerator = random.Random(millisecondsSinceMidnight)
        self._DeepLId = baseIdMult * round(baseIdMult * randomGenerator.random())

    def requestTranslation(
        self,
        url: str,
        text: str,
        targetLang: str,
        sourceLang: str,
    ) -> str:
        """Build a DeepL JSON-RPC request, send it and parse translated sentences."""

        if sourceLang.lower() == targetLang.lower():
            return text

        preparedText = self._preprocess(text)
        sentences = [
            match.group(1)
            for match in re.finditer(self._regex, preparedText)
        ]

        if not sentences:
            sentences.append(preparedText)

        jobs = []
        for index, sentence in enumerate(sentences):
            contextBefore = [sentences[index - 1]] if index > 0 else []
            contextAfter = (
                [sentences[index + 1]]
                if index + 1 < len(sentences)
                else []
            )

            jobs.append(
                {
                    "kind": "default",
                    "raw_en_sentence": sentence,
                    "raw_en_context_before": contextBefore,
                    "raw_en_context_after": contextAfter,
                    "preferred_num_beams": 0,
                }
            )

        sourceLanguage = sourceLang.upper()
        targetLanguage = targetLang.upper()

        body = {
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": jobs,
                "lang": {
                    "user_preferred_langs": [
                        sourceLanguage,
                        targetLanguage,
                    ],
                    "source_lang_computed": sourceLanguage,
                    "target_lang": targetLanguage,
                },
                "priority": 1,
                "commonJobParams": None,
                "timestamp": int(time.time() * 1000),
            },
            "id": self._DeepLId,
        }

        session = getattr(self, "_session", None)
        if session is None:
            self._createDeeplSession()
            session = self._session

        try:
            response = session.post(
                url,
                data = json.dumps(body, ensure_ascii=False),
                timeout = self._requestTimeout,
            )
            self._DeepLId += 1
            response.raise_for_status()
            answer = response.json()
        except (RequestException, ValueError) as error:
            self.logger.error(f"DeepL request failed: {error}")
            return ""

        translations = answer.get("result", {}).get("translations")
        if not translations:
            self.logger.error(
                "DeepL strange response; translations are missing: "
                f"{response.text}"
            )
            return ""

        translatedSentences = []
        for translation in translations:
            beams = translation.get("beams") or []
            if not beams:
                continue

            translatedSentence = beams[0].get("postprocessed_sentence")
            if translatedSentence is not None:
                translatedSentences.append(translatedSentence)

        return " ".join(translatedSentences)

    def _createDeeplSession(self) -> None:
        """ Create Deepl session"""

        previousSession = getattr(self, "_session", None)
        if previousSession is not None:
            previousSession.close()

        session = Session()
        session.headers.update(
            {
                "Accept": "*/*",
                "Referer": "https://www.deepl.com/translator",
                "Content-Type": "application/json",
                "Accept-Language": "en-US;q=0.5,en;q=0.3",
                "DNT": "1",
                "TE": "Trailers",
            }
        )
        self._session = session

    @staticmethod
    def _preprocess(text: str) -> str:
        return text.replace("\u2014", "-")

    @property
    def baseUrl(self) -> str:
        return self._baseUrl

    @property
    def textLimit(self) -> int:
        return TranslatorsLimit.fromValue(Translators.DEEPL)
