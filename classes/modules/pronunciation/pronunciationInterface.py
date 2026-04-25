# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class PronunciationInterface(ABC):

    @abstractmethod
    def pronounceText(self) -> None: raise NotImplementedError
