from classes.menu.actions.actionInterface import ActionInterface
from classes.services.translatorFactory import TranslatorFactory
from classes.enums.routes import Routes


class PrepareTranslateAction(ActionInterface):
    def __init__(self, ui, loadLang, navigator):
        self.ui = ui
        self.loadLang = loadLang
        self.navigator = navigator

        self.ui.translateWindow.clicked.connect(self.execute)

    def execute(self) -> None:
        """
           Preparation before the translation 
        """
        
        if self.ui.stackedWidget.currentIndex() != Routes.TRANSLATE.value:
            self.navigator.goTo(Routes.TRANSLATE)
            return
        
        if not self.ui.inputBox.toPlainText():
            return

        self.ui.translateBox.clear()
        text = self.ui.inputBox.toPlainText()
        
        #If leave the formatting
        if self.ui.actionLeaveTheFormatting.isChecked():
            text = self.ui.inputBox.toHtml()
        
        translator = TranslatorFactory().getTranslator(self.ui.currentTranslator)
        translatedText = translator.translate(
            text, 
            self.loadLang.getKeyLang(self.ui.toLang.currentText()),
            self.loadLang.getKeyLang(self.ui.fromLang.currentText())
        )
        self.ui.translateBox.insertHtml(translatedText)
