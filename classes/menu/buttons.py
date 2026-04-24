from PyQt6.QtWidgets import QApplication
from classes.translate.googleTranslator import *
from classes.translate.deeplTranslator import *
from classes.modules.pronunciation.pronunciation import *
from classes.logger import *
from classes.enums.Translate.translators import Translators


class Buttons():
    """
        Main program buttons
    """

    def __init__(self, ui, db, loadLang, navigator, flashCards):
        self.ui = ui
        self.db = db
        self.loadLang = loadLang
        self.navigator = navigator
        self.flashCards = flashCards

    def clearTranslate(self, eve) -> None:
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

    def copyToClipboard(self, eve) -> None:
        """
            Copy text to clipboard
        """
        
        QApplication.clipboard().setText(self.ui.translateBox.toPlainText())

    def reverseTranslations(self, eve) -> None:
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

    def saveTranslatedText(self, eve) -> None:
        """
           Save translated text to DB
        """

        if self.ui.translateBox.toPlainText() == '':
            return None
        
        self.db.insertTranslate()   

    def pronunciation(self, eve) -> None:
        """
            Text pronunciation
        """

        if self.ui.translateBox.toPlainText() == '':
            return None

        Pronunciation(self.ui.translateBox.toPlainText())
