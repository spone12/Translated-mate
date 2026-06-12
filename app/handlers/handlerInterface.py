# Main Interface program handlers
from abc import ABC, ABCMeta, abstractmethod


class HandlerInterface(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs): raise NotImplementedError
