from .abstractAction import AbstractAction
from classes.services.translationHistory import TranslationHistory


class NextTranslationAction(AbstractAction):
    def __init__(self, ui, history: TranslationHistory):
        self.ui = ui
        self.history = history
        
        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Previous translation action
        """
        
        self.history.forward()

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.nextTranslate
