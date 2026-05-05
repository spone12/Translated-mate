from classes.modules.pronunciation.pronunciation import Pronunciation
from .abstractAction import AbstractAction


class SourcePronunciationAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Text pronunciation action
        """
        
        if not self.ui.inputBox.toPlainText():
            return None

        Pronunciation(self.ui.inputBox.toPlainText())

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.sourcePronunciation
