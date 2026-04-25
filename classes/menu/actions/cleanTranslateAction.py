from PyQt6.QtWidgets import QApplication
from classes.menu.actions.actionInterface import ActionInterface


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
