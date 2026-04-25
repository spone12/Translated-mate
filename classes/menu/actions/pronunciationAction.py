from classes.menu.actions.actionInterface import ActionInterface
from classes.modules.pronunciation.pronunciation import Pronunciation


class PronunciationAction(ActionInterface):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.ui.pronunciation.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Text pronunciation action
        """
        
        if not self.ui.translateBox.toPlainText():
            return None

        Pronunciation(self.ui.translateBox.toPlainText())
