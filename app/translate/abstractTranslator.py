# Abstract translator class
from abc import abstractmethod
from .translateInterface import TranslateInterface
from app.core.logger import Logger
from textwrap import wrap


class AbstractTranslator(TranslateInterface):

    def __init__(self):
        self.logger = Logger().getLogger(self.__class__.__name__)
        
    @property
    @abstractmethod
    def baseUrl(self) -> str: raise NotImplementedError

    @property
    @abstractmethod
    def textLimit(self) -> int: raise NotImplementedError

    def textLimitReached(self, text: str) -> bool:
        """ Check if text limit has been reached """
        return len(text) >= self.textLimit

    def getTextChunks(self, text: str, len: int) -> list:
        """ Splitting large text into chunks """
        return wrap(text, len)
