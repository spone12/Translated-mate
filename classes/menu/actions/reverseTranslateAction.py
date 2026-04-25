from classes.menu.actions.actionInterface import ActionInterface


class ReverseTranslateAction(ActionInterface):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.ui.reverseTranslate.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Flip the translations around
        """
    
        fromLangIndex = self.ui.fromLang.currentIndex()
        toLangIndex = self.ui.toLang.currentIndex()

        inputBoxText = self.ui.inputBox.toHtml()
        translateBoxText = self.ui.translateBox.toHtml()
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

        self.ui.translateBox.insertHtml(inputBoxText)
        self.ui.inputBox.insertHtml(translateBoxText)

        self.ui.toLang.setCurrentIndex(fromLangIndex)
        self.ui.fromLang.setCurrentIndex(toLangIndex)
