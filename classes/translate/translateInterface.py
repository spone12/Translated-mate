# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class TranslateInterface(ABC):

    @property
    @abstractmethod
    def baseUrl(self) -> str: raise NotImplementedError

    @property
    @abstractmethod
    def textLimit(self) -> int: raise NotImplementedError

    @abstractmethod
    def translate(self, text: str, targetLang: str, sourceLang: str = 'auto') -> str: raise NotImplementedError

    @abstractmethod
    def requestTranslation(self, url: str, *args, **kwargs) -> str: raise NotImplementedError
