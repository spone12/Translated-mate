# Abstract handler class
from abc import abstractmethod
from .handlerInterface import HandlerInterface


class AbstractHandler(HandlerInterface):
    
    def __init__(self, ui):
        self.ui = ui
        self.bind()
        
    @abstractmethod
    def bind(self) -> None:
        """ Bind the handler """
        pass
