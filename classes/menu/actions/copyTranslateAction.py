from PyQt6.QtWidgets import QApplication
from .abstractAction import AbstractAction

class CopyTranslateAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.widget.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Copy translated text to clipboard
        """
        
        QApplication.clipboard().setText(self.ui.translateBox.toPlainText())
        self.showTooltip("Copied")

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.copyTranslate
