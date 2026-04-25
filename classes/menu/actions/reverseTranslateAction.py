from classes.menu.actions.actionInterface import ActionInterface


class ReverseTranslateAction(ActionInterface):
    def __init__(self, ui):
        self.ui = ui
        self.ui.reverseTranslate.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Flip the translations around
        """
    
        currentToIndex = self.ui.toLang.currentIndex()
        currentFromIndex = self.ui.fromLang.currentIndex()
        inputText = self.ui.inputBox.toHtml()
        translateBox = self.ui.translateBox.toHtml()
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()
        self.ui.translateBox.insertHtml(inputText)
        self.ui.inputBox.insertHtml(translateBox)
        self.ui.toLang.setCurrentIndex(currentFromIndex)
        self.ui.fromLang.setCurrentIndex(currentToIndex)
