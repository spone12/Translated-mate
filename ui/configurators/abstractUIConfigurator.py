from abc import abstractmethod
from .configuratorInterface import ConfiguratorInterface

class AbstractUIConfigurator(ConfiguratorInterface):
    def __init__(self, ui):
        self.ui = ui

    def apply(self):
        """ Method call """
        
        self.setupUiProperties()
    
    def setProperty(self, widget, role, value = True):
        """ Setup Property """
        
        widget.setProperty(role, value)
        
    @abstractmethod
    def setupUiProperties(self) -> None:
        """ Setup UI properties """
        pass
