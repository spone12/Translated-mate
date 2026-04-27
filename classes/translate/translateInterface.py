# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class TranslateInterface(ABC):

    @abstractmethod
    def translate(self, text: str, targetLang: str, sourceLang = '') -> str: raise NotImplementedError

    @abstractmethod
    def translateIternal(self, formattedUrl: str): raise NotImplementedError

