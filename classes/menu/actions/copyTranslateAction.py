from PyQt6.QtWidgets import QApplication
from classes.menu.actions.actionInterface import ActionInterface


class CopyTranslateAction(ActionInterface):
    def __init__(self, ui):
        self.ui = ui
        self.ui.copyTranslate.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Copy translated text to clipboard
        """
        
        QApplication.clipboard().setText(self.ui.translateBox.toPlainText())
