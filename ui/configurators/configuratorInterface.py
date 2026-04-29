# Main Interface translations API
from abc import ABC, ABCMeta, abstractmethod


class ConfiguratorInterface(ABC):

    @abstractmethod
    def apply(self) -> None: raise NotImplementedError
