# Abstract translator class
from abc import abstractmethod
from .translateInterface import TranslateInterface
from textwrap import wrap

class AbstractTranslator(TranslateInterface):

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
    