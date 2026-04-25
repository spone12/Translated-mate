# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class WindowInterface(ABC):

    @abstractmethod
    def prepareWindow(self) -> None: raise NotImplementedError
