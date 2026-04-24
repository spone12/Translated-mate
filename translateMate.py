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
from classes.enums.Translate.translators import Translators
from classes.menu.actions.prepareTranslateAction import PrepareTranslateAction


class TranslateMate(QtWidgets.QMainWindow):
    """
        Main program launch class
    """

    def __init__(self):

        super(self.__class__, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        self.ui.currentTranslator = Translators.GOOGLE
        
        self.styles = Styles(self)
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        self.loadLang = LoadingLangs(self.ui)
        self.menu = Menu(self)
        self.db = DB(self.ui)
        self.savedTranslation = SavedTranslationWindow(self.ui, self.db)
        self.flashCards = FlashCardsWindow(self.ui, self.db)
        self.buttons = Buttons(
            self.ui,
            self.db,
            self.loadLang,
            self.navigator,
            self.savedTranslation,
            self.flashCards
        )

        self.programEvents()

        
    def programEvents(self) -> None:
        """
            Loading program events
        """

        # Actions
        self.actions = [
            PrepareTranslateAction(self.ui, self.loadLang)
        ]
        
        self.ui.saveTranslatedText.clicked.connect(self.buttons.saveTranslatedText)
        self.ui.reverseTranslate.clicked.connect(self.buttons.reverseTranslations)
        self.ui.clearInput.clicked.connect(self.buttons.clearTranslate)
        self.ui.copyTranslate.clicked.connect(self.buttons.copyToClipboard)
        self.ui.pronunciation.clicked.connect(self.buttons.pronunciation)

        # Windows
        self.ui.saveTranslationWindow.clicked.connect(
            lambda: self.buttons.changeWindow(self.savedTranslation.QSindex)
        )

        self.ui.flashCardsWindow.clicked.connect(
            lambda: self.buttons.changeWindow(self.flashCards.QSindex)
        )

        # Triggers
        self.ui.actionExit.triggered.connect(self.menu.exitProgramm)
        self.ui.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
