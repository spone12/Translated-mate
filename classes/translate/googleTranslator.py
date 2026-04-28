# Google translate
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import urllib.parse
from classes.translate.translateInterface import TranslateInterface
from classes.logger import Logger
import time
import math
from textwrap import wrap


class GoogleTranslator(TranslateInterface):
    """
        Google translate class
    """

    _baseUrl   = "https://translate.google.com/m?hl=ru&sl={0}&tl={1}&ie=UTF-8&prev=_m&q={2}"
    TEXT_LIMIT = 10000

    def translate(self, text: str, targetLang: str, sourceLang: str = 'auto') -> str:
        """
            Main tranlate method
        """

        translatedText = ''

        if len(text) > 5000:

            #Splitting large text into chunks
            chunkedText = wrap(text, 5000)

            for currentTextBlock in chunkedText:
                translatedText += self.requestTranslation(
                    self.formatUrl(sourceLang, targetLang, currentTextBlock)
                )
                time.sleep(0.300)
        else:
            translatedText = self.requestTranslation(
                self.formatUrl(sourceLang, targetLang, text)
            )

        return translatedText

    def formatUrl(self, sourceLang: str, targetLang: str, text: str) -> str:
        """
            Format the source URL
        """

        return self.baseUrl.format(sourceLang, targetLang, urllib.parse.quote(text, safe = ""))

    def requestTranslation(self, url: str) -> str:
        """
            Request a source for text translation
        """
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Opera/9.80 (Android; Opera Mini/11.0.1912/37.7549; U; pl) Presto/2.12.423 Version/12.16',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        parsedAnswer = ''

        try:
            request = requests.get(url, headers = headers)
            request.raise_for_status()
        except HTTPError as http_err:
            Logger().log(self.__class__.__name__, f"HTTP error occurred: {http_err}")
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Other error occurred: {err}")
        else:
            answer       = BeautifulSoup(request.text, 'html.parser')
            parsedAnswer = answer.find('div', class_='result-container').text
           
        return parsedAnswer

    @property
    def baseUrl(self) -> str:
        return self._baseUrl
    
    @property
    def textLimit(self) -> int:
        return self.TEXT_LIMIT
    