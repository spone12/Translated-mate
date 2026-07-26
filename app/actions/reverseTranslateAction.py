from .abstractAction import AbstractAction


class ReverseTranslateAction(AbstractAction):
    def __init__(self, ui, speechService):
        self.ui = ui
        self.speechService = speechService

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Flip the translations around
        """
        
        # Disable voice speach recognize
        self.speechService.stop()
        
        sourceLangIndex = self.ui.sourceLangList.currentIndex()
        targetLangIndex = self.ui.targetLangList.currentIndex()

        inputBoxText = self.ui.inputBox.toHtml()
        translateBoxText = self.ui.translateBox.toHtml()
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

        self.ui.translateBox.insertHtml(inputBoxText)
        self.ui.inputBox.insertHtml(translateBoxText)

        self.ui.targetLangList.setCurrentIndex(sourceLangIndex)
        self.ui.sourceLangList.setCurrentIndex(targetLangIndex)

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.reverseTranslate
