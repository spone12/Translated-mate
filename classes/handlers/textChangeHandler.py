from .abstractHandler import AbstractHandler
from classes.core.validators.translationValidator import TranslationValidator
from classes.core.controllers.translationFormController import TranslationFormController


class TextChangeHandler(AbstractHandler):
    
    def __init__(self, ui):
        self.controller = TranslationFormController(TranslationValidator())
        super().__init__(ui)
        
        self.sourceButtons = [
            self.ui.sourceCopyTranslate,
            self.ui.sourcePronunciation,
            self.ui.cleanTranslate,
        ]
        
        self.translateButtons = [
            self.ui.copyTranslate,
            self.ui.pronunciation,
        ]
        
    def bind(self) -> None:
        """ Bind the handler """
        self.ui.inputBox.textChanged.connect(self.execute)

    def execute(self) -> None:
        """ Triggering events when the input field is changed """
        
        state = self.controller.getState(
            self.ui.inputBox.toPlainText(),
            self.ui.translateBox.toPlainText(),
        )
        self.updateUI(state)
    
    def updateUI(self, state: list) -> None:
        """ Update UI """

        for btn in self.sourceButtons:
            btn.setEnabled(state["is_valid"])
        
        
        for btn in self.translateButtons:
            btn.setEnabled(state["is_valid_target"])
        
        self.ui.saveTranslatedText.setEnabled(state["can_save"])
        
        # Char counter
        #self.ui.charCounter.setText(str(state["length"]))
