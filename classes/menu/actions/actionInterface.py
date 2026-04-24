# Main Interface program actions
from abc import ABC, ABCMeta, abstractmethod


class ActionInterface(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs): raise NotImplementedError
