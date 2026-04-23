# Translate mate
# Version 0.4
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from ui.ui_main_window import Ui_MainWindow
from classes.navigator.navigator import Navigator
from classes.styles.styles import Styles
from classes.translate.googleTranslator import *
from classes.translate.TranslationResources.loadLangs import LoadingLangs
from classes.menu.menu import Menu
from classes.menu.buttons import Buttons
from classes.windows.savedTranslationWindow import *
from classes.windows.flashCardsWindow import *
from classes.db import *

class TranslateMate(QtWidgets.QMainWindow):
    """
        Main program launch class
    """

    def __init__(self):

        super(self.__class__, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        self.ui.currentTranslator = 'Google'
        
        self.styles = Styles(self)
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        self.loadLang = LoadingLangs(self.ui)
        self.menu = Menu(self)
        self.ui.db = DB(self.ui)
        self.ui.savedTranslation = SavedTranslationWindow(self.ui)
        self.ui.flashCards = FlashCardsWindow(self.ui)
        self.buttons = Buttons(
            self.ui,
            self.loadLang,
            self.navigator,
            self.ui.savedTranslation,
            self.ui.flashCards
        )

        self.programEvents()

        
    def programEvents(self) -> None:
        """
            Loading program events
        """

        # Buttons
        self.ui.translateWindow.clicked.connect(self.buttons.prepareTranslate)
        self.ui.saveTranslatedText.clicked.connect(self.buttons.saveTranslatedText)
        self.ui.reverseTranslate.clicked.connect(self.buttons.reverseTranslations)
        self.ui.clearInput.clicked.connect(self.buttons.clearTranslate)
        self.ui.copyTranslate.clicked.connect(self.buttons.copyToClipboard)
        self.ui.pronunciation.clicked.connect(self.buttons.pronunciation)

        # Windows
        self.ui.saveTranslationWindow.clicked.connect(
            lambda: self.buttons.changeWindow(self.ui.savedTranslation.QSindex)
        )

        self.ui.flashCardsWindow.clicked.connect(
            lambda: self.buttons.changeWindow(self.ui.flashCards.QSindex)
        )

        # Triggers
        self.ui.actionExit.triggered.connect(self.menu.exitProgramm)
        self.ui.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
