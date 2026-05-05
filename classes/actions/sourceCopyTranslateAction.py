from PyQt6.QtWidgets import QApplication
from .abstractAction import AbstractAction


class SourceCopyTranslateAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Copy translated text to clipboard
        """
        
        if not self.ui.inputBox.toPlainText():
            return None
        
        QApplication.clipboard().setText(self.ui.inputBox.toPlainText())
        self.showTooltip("Copied")

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.sourceCopyTranslate
