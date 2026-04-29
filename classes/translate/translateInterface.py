# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class TranslateInterface(ABC):

    @abstractmethod
    def translate(self, text: str, targetLang: str, sourceLang: str = 'auto') -> str: raise NotImplementedError

    @abstractmethod
    def requestTranslation(self, url: str, *args, **kwargs) -> str: raise NotImplementedError

    @abstractmethod
    def textLimitReached(self, text: str) -> bool: raise NotImplementedError
    