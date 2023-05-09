# Google translate
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import urllib.parse
from classes.translate.translateInterface import *
from classes.logger import *


class GoogleTranslator(TranslateInterface):
    """
        Google translate class
    """

    def translate(self, text: str, toLang: str, fromLang = 'auto') -> str:

       _baseUrl    = "https://translate.google.com/m?hl=ru&sl={0}&tl={1}&ie=UTF-8&prev=_m&q={2}"
       formatedUrl = _baseUrl.format(fromLang, toLang, urllib.parse.quote(text, safe = ""))

       return self.translateIternal(formatedUrl)

    
    def translateIternal(self, formatedUrl: str):
        
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
            request = requests.get(formatedUrl, headers = headers)
            request.raise_for_status()
        except HTTPError as http_err:
            Logger().log(self.__class__.__name__, f"HTTP error occurred: {http_err}")
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Other error occurred: {err}")
        else:
            answer       = BeautifulSoup(request.text, 'html.parser')
            parsedAnswer = answer.find('div', class_='result-container').text
           
        return parsedAnswer
