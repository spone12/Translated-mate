# Translate mate
# Version 0.4.2
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_main_window import Ui_MainWindow
from classes.core.navigator import Navigator
from classes.styles.styles import Styles
from classes.translate.TranslationResources.loadLangs import LoadingLangs
from classes.menu.menu import Menu
from classes.windows.savedTranslationWindow import SavedTranslationWindow
from classes.windows.flashCardsWindow import FlashCardsWindow
from classes.db import DB
from classes.enums.Translate.translators import Translators
from classes.enums.routes import Routes
from classes.menu.actions.prepareTranslateAction import PrepareTranslateAction
from classes.menu.actions.pronunciationAction import PronunciationAction
from classes.menu.actions.saveTranslatedTextAction import SaveTranslatedTextAction
from classes.menu.actions.reverseTranslateAction import ReverseTranslateAction
from classes.menu.actions.copyTranslateAction import CopyTranslateAction
from classes.menu.actions.cleanTranslateAction import CleanTranslateAction


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

        self.programEvents()

        
    def programEvents(self) -> None:
        """
            Loading program events
        """
        
        self.navigator.register(Routes.SAVED, self.savedTranslation.prepareWindow)
        self.navigator.register(Routes.FLASHCARDS, self.flashCards.prepareWindow)

        # Actions
        self.actions = [
            PrepareTranslateAction(self.ui, self.loadLang, self.navigator),
            SaveTranslatedTextAction(self.ui, self.db),
            PronunciationAction(self.ui),
            CopyTranslateAction(self.ui),
            CleanTranslateAction(self.ui),
            ReverseTranslateAction(self.ui)
        ]

        # Windows
        self.ui.saveTranslationWindow.clicked.connect(
            lambda: self.navigator.goTo(Routes.SAVED)
        )

        self.ui.flashCardsWindow.clicked.connect(
            lambda: self.navigator.goTo(Routes.FLASHCARDS)
        )

        # Triggers
        self.ui.actionExit.triggered.connect(self.menu.exitProgramm)
        self.ui.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
