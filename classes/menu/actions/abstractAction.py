# Abstract action class
from abc import abstractmethod
from .actionInterface import ActionInterface
from ui.widgets.persistantTooltip import PersistentTooltip

class AbstractAction(ActionInterface):

    @property
    @abstractmethod
    def widget(self): raise NotImplementedError

    def showTooltip(self, text: str) -> None:
        """ Show message tooltip """
        pos = self.widget.mapToGlobal(
            self.widget.rect().bottomRight()
        )
        PersistentTooltip(self.widget).showText(pos, text)
