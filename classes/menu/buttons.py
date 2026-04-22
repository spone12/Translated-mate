from PyQt6.QtWidgets import QApplication
from classes.translate.googleTranslator import *
from classes.translate.deeplTranslator import *
from classes.modules.pronunciation.pronunciation import *


class Buttons():
    """
        Main program buttons
    """

    def __init__(self, ui, loadLang):
        self.ui = ui
        self.loadLang = loadLang

    def clearTranslate(self, eve) -> None:
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

    def changeWindow(self, QSIndex) -> None:
        """
           Change Window
        """

        windows = [self.ui.translateWindow, self.ui.saveTranslationWindow, self.ui.flashCardsWindow]
        for w in windows:
            w.setStyleSheet(w.styleSheet().replace('background-color: #fff6f7;', ''))

        match QSIndex:
            case 0:
                self.ui.stackedWidget.setCurrentIndex(QSIndex)
            case 1:
                self.ui.savedTranslation.changeWindow()
            case 2:
                self.ui.flashCards.changeWindow() 

        for ind, w in enumerate(windows):
            if (ind == QSIndex):
                w.setStyleSheet(w.styleSheet().replace('no-repeat;', 'no-repeat;background-color: #fff6f7;'))

    def copyToClipboard(self, eve) -> None:
        
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

    def prepareTranslate(self, eve) -> None:
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
        
        #if leave the formatting
        if self.ui.actionLeaveTheFormatting.isChecked():
            text = self.ui.inputBox.toHtml()
        
        match self.ui.currentTranslator:
            case 'Google':
                translator = GoogleTranslator()
            case 'Deepl':
                translator = DeeplTranslator()
        
        translated = translator.translate(
            text, 
            self.loadLang.getKeyLang(self.ui.toLang.currentText()),
            self.loadLang.getKeyLang(self.ui.fromLang.currentText())
        )
        self.ui.translateBox.insertHtml(translated)

    def saveTranslatedText(self, eve) -> None:
        """
           Save translated text to DB
        """

        if self.ui.translateBox.toPlainText() == '':
            return None
        
        self.ui.db.insertTranslate()   

    def pronunciation(self, eve) -> None:
        """
            Text pronunciation
        """

        if self.ui.translateBox.toPlainText() == '':
            return None

        Pronunciation(self.ui.translateBox.toPlainText())
