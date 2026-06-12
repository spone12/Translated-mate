from PyQt6.QtWidgets import QApplication
from .abstractAction import AbstractAction


class CopyTranslateAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Copy translated text to clipboard
        """
        
        if not self.ui.translateBox.toPlainText():
            return None
        
        QApplication.clipboard().setText(self.ui.translateBox.toPlainText())
        self.showTooltip("Copied")

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.copyTranslate
