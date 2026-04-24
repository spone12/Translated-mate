from classes.menu.actions.actionInterface import ActionInterface
from classes.enums.Translate.translators import Translators
from classes.translate.googleTranslator import GoogleTranslator
from classes.translate.deeplTranslator import DeeplTranslator


class PrepareTranslateAction(ActionInterface):
    def __init__(self, ui, loadLang):
        self.ui = ui
        self.loadLang = loadLang

        self.ui.translateWindow.clicked.connect(self.execute)

    def execute(self):
        """
           Preparation before the translation 
        """
        
        if self.ui.stackedWidget.currentIndex() != 0:
            self.changeWindow(0)
            return
        
        if not self.ui.inputBox.toPlainText():
            return

        self.ui.translateBox.clear()
        text = self.ui.inputBox.toPlainText()
        
        #If leave the formatting
        if self.ui.actionLeaveTheFormatting.isChecked():
            text = self.ui.inputBox.toHtml()
        
        match self.ui.currentTranslator:
            case Translators.GOOGLE:
                translator = GoogleTranslator()
            case Translators.DEEPL:
                translator = DeeplTranslator()
        
        translated = translator.translate(
            text, 
            self.loadLang.getKeyLang(self.ui.toLang.currentText()),
            self.loadLang.getKeyLang(self.ui.fromLang.currentText())
        )
        self.ui.translateBox.insertHtml(translated)
