# Translate mate
# Version 0.4.3
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_main_window import Ui_MainWindow
from classes.core.navigator import Navigator
from classes.styles.styles import Styles
from classes.translate.TranslationResources.loadLangs import LoadingLangs
from classes.menu.menu import Menu
from classes.windows.TranslationViewWindow import TranslationViewWindow
from classes.windows.flashCardsWindow import FlashCardsWindow
from classes.db import DB
from classes.enums.Translate.translators import Translators
from classes.enums.routes import Routes
from classes.menu.actions.translateAction import TranslateAction
from classes.menu.actions.pronunciationAction import PronunciationAction
from classes.menu.actions.saveTranslatedTextAction import SaveTranslatedTextAction
from classes.menu.actions.reverseTranslateAction import ReverseTranslateAction
from classes.menu.actions.copyTranslateAction import CopyTranslateAction
from classes.menu.actions.cleanTranslateAction import CleanTranslateAction
from classes.menu.actions.goToRouteAction import GoToRouteAction


class TranslateMate(QtWidgets.QMainWindow):
    """
        Main program launch class
    """

    def __init__(self):

        super(self.__class__, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DB(self.ui)

        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        self.ui.currentTranslator = Translators.GOOGLE
        
        self.styles = Styles(self)
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        self.loadLang = LoadingLangs(self.ui)
        self.menu = Menu(self, self.db)
        self.translationView = TranslationViewWindow(self.ui, self.db)
        self.flashCards = FlashCardsWindow(self.ui, self.db)

        self.programEvents()

        
    def programEvents(self) -> None:
        """
            Loading program events
        """
        
        # Actions
        self.actions = [
            TranslateAction(self.ui, self.loadLang, self.navigator),
            SaveTranslatedTextAction(self.ui, self.db),
            PronunciationAction(self.ui),
            CopyTranslateAction(self.ui),
            CleanTranslateAction(self.ui),
            ReverseTranslateAction(self.ui)
        ]

        # Action routes
        self.actions += [
            GoToRouteAction(self.ui.TranslationViewWindow, self.navigator, Routes.SAVED, self.translationView.prepareWindow),
            GoToRouteAction(self.ui.FlashCardsWindow, self.navigator, Routes.FLASHCARDS, self.flashCards.prepareWindow)
        ]

        # Triggers
        self.ui.actionExit.triggered.connect(self.menu.exitProgramm)
        self.ui.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
