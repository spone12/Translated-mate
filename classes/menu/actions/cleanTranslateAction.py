from classes.menu.actions.actionInterface import ActionInterface
from ui.widgets.persistantTooltip import PersistentTooltip

class CleanTranslateAction(ActionInterface):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.ui.cleanTranslate.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Clean input and translated text
        """
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()
        
        """ TODO: create abstract class """
        pos = self.ui.cleanTranslate.mapToGlobal(self.ui.cleanTranslate.rect().bottomRight())
        PersistentTooltip(self.ui.cleanTranslate).showText(pos, "Cleaned")
