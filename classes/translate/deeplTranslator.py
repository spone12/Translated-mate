# Deepl translate
import requests
from requests.exceptions import HTTPError
from classes.translate.translateInterface import TranslateInterface
from classes.logger import Logger
import time
import math
from textwrap import wrap
import random
import calendar
import json
import datetime
import re


class DeeplTranslator(TranslateInterface):
    """
        Deepl translate class
    """

    _baseUrl   = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'
    TEXT_LIMIT = 1500
    _DeepLId   = 0
    _regex     = "(\S.+?([.!?♪。]|$))(?=\s+|$)"

    def translate(self, text: str, targetLang: str, sourceLang: str = 'auto') -> str:
        """
            Main tranlate method
        """
        
        self.generateDeeplId()
        return self.requestTranslation(self.baseUrl, text, targetLang, sourceLang)

    def generateDeeplId(self) -> None:

        baseIdMult = 10000
        currentTime = time.strptime(str(datetime.datetime.now().time()).split('.')[0], '%H:%M:%S')
        totalSeconds = datetime.timedelta(
            hours   = currentTime.tm_hour,
            minutes = currentTime.tm_min,
            seconds = currentTime.tm_sec).total_seconds() * 1000
        Rnd = random.Random(totalSeconds)
        self._DeepLId = baseIdMult * round(baseIdMult * Rnd.random())
        

    def requestTranslation(self, url: str, text: str, targetLang: str, sourceLang: str) -> str:
        """
            Request a source for text translation
        """
        
        headers = {
            'Accept': '*/*',
            'Referer': 'https://www.deepl.com/translator',
            'Content-type': 'application/json',
            'Cache-Control': 'no-cache',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'DNT': '1',
            'TE': 'Trailers',
            'User-Agent': 'Opera/9.80 (Android; Opera Mini/11.0.1912/37.7549; U; pl) Presto/2.12.423 Version/12.16'
        }

        matchSentences = re.findall(self._regex, text)
        jobs = []

        # Generate Jobs
        lengthMatches = len(matchSentences)
        for k, sentence in enumerate(matchSentences):

            afterString = []
            if (k + 1) < lengthMatches:
                afterString.append(matchSentences[k + 1][0])

            beforeSentences = []
            if k > 0:
                for n in range(k):
                    beforeSentences.append(matchSentences[n][0])

            job = {
                    "kind": "default",
                    "preferred_num_beams": 4,
                    "quality": "fast",
                    "raw_en_context_after": afterString,
                    "raw_en_context_before": beforeSentences,
                    "sentences": [
                        {
                            "id":  (k + 1),
                            "prefix": "",
                            "text": sentence[0]
                        }
                    ]
                }

            jobs.append(job)
        
        timestamp = calendar.timegm(time.gmtime()) * 1000
        body = {
            "id": self._DeepLId,
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "commonJobParams": {
                    "browserType": 1,
                    "mode": "translate",
                    "textType": "plaintext"
                },
                "jobs": jobs,
                "lang": {
                    "preference": {
                        "default": "default",
                        "weight": {}
                    },
                    "source_lang_computed": sourceLang.upper(),
                    "target_lang": targetLang.upper()
                },
                "priority": -1,
                "timestamp": timestamp
            }
        }

        parsedAnswer = ""
        
        try:
            request = requests.post(url, data=json.dumps(body), headers = headers)
            request.raise_for_status()
        except HTTPError as http_err:
            Logger().log(self.__class__.__name__, f"HTTP error occurred: {http_err}")
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Other error occurred: {err}")
        else:

            answerDecode = json.loads(request.text)
            if not answerDecode['result']['translations']:
                Logger().log(self.__class__.__name__, f"Deepl strange response;")
                Logger().log(self.__class__.__name__, f"Deepl body is null!")

            for trans in answerDecode['result']['translations']:
                parsedAnswer += trans['beams'][0]['sentences'][0]['text']
        
        return parsedAnswer

    @property
    def baseUrl(self) -> str:
        return self._baseUrl
    
    @property
    def textLimit(self) -> int:
        return self.TEXT_LIMIT
    