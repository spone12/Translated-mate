# Abstract action class
from abc import abstractmethod
from .actionInterface import ActionInterface
from ui.widgets.persistantTooltip import PersistentTooltip
from app.enums.routes import Routes
from ui.widgets.actionTooltip import ActionTooltip
from app.core.actionRouter import ActionRouter


class AbstractAction(ActionInterface):

    def __init__(self):
        self.toast = None
        
    @property
    @abstractmethod
    def widget(self): raise NotImplementedError

    def bind(self) -> None:
        """ Bind the action """
        if self.widget:
            self.widget.clicked.connect(self.execute)
    
    def bindToast(self, actionRouter: ActionRouter, route: Routes):
        """ Bind toast to route """
        actionRouter.bind(self.getToast().clicked, route)
        
    def showTooltip(self, text: str) -> None:
        """ Show message tooltip """
        pos = self.widget.mapToGlobal(
            self.widget.rect().bottomRight()
        )
        PersistentTooltip(self.widget).showText(pos, text)

    def getToast(self):
        """ Get toast """
        
        if self.toast is None:
            self.toast = ActionTooltip(self.widget)
        return self.toast
