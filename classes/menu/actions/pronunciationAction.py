from classes.modules.pronunciation.pronunciation import Pronunciation
from .abstractAction import AbstractAction

class PronunciationAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.widget.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Text pronunciation action
        """
        
        if not self.ui.translateBox.toPlainText():
            return None

        Pronunciation(self.ui.translateBox.toPlainText())

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.pronunciation
