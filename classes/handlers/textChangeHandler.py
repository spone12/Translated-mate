from .abstractHandler import AbstractHandler
from classes.core.validators.translationValidator import TranslationValidator
from classes.core.controllers.formController import FormController


class TextChangeHandler(AbstractHandler):
    
    def __init__(self, ui):
        self.controller = FormController(TranslationValidator())
        super().__init__(ui)
        
    def bind(self) -> None:
        """ Bind the handler """
        self.ui.inputBox.textChanged.connect(self.execute)

    def execute(self) -> None:
        """ Triggering events when the input field is changed """
        
        state = self.controller.getState(
            self.ui.inputBox.toPlainText()
        )
        self.updateUI(state)
    
    def updateUI(self, state: list) -> None:
        """ Update UI """
        
        buttons = [
            self.ui.sourceCopyTranslate,
            self.ui.copyTranslate,
            self.ui.sourcePronunciation,
            self.ui.pronunciation,
            self.ui.cleanTranslate,
            self.ui.saveTranslatedText,
        ]

        for btn in buttons:
            btn.setEnabled(state["is_valid"])

        # Char counter
        #self.ui.charCounter.setText(str(state["length"]))
