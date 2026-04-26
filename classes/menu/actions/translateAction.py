from classes.menu.actions.actionInterface import ActionInterface
from classes.services.translatorFactory import TranslatorFactory
from classes.enums.routes import Routes


class TranslateAction(ActionInterface):
    def __init__(self, ui, loadLang, navigator):
        self.ui = ui
        self.loadLang = loadLang
        self.navigator = navigator

        # UI subscription
        self.ui.TranslateWindow.clicked.connect(self.execute)

    def execute(self) -> None:
        """
           Preparation before the translation 
        """
        
        if self.ui.DisplayArea.currentIndex() != Routes.TRANSLATE.value:
            self.navigator.goTo(Routes.TRANSLATE)
            return
        
        text = self.ui.inputBox.toPlainText()
        if not text:
            return
        
        self.ui.translateBox.clear()
        
        # If leave the formatting
        if self.ui.actionLeaveTheFormatting.isChecked():
            text = self.ui.inputBox.toHtml()
        
        translator = TranslatorFactory().getTranslator(self.ui.currentTranslator)
        translatedText = translator.translate(
            text, 
            self.loadLang.getKeyLang(self.ui.toLang.currentText()),
            self.loadLang.getKeyLang(self.ui.fromLang.currentText())
        )
        self.ui.translateBox.insertHtml(translatedText)
