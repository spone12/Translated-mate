# Translate mate
# Version 0.4.5
import sys
import ctypes
from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_main_window import Ui_MainWindow
from classes.core.navigator import Navigator
from classes.styles.styles import Styles
from ui.configurators.mainWindowConfigurator import MainWindowConfigurator
from classes.translate.TranslationResources.loadLangs import LoadingLangs
from classes.menu.menu import Menu
from classes.windows.TranslationViewWindow import TranslationViewWindow
from classes.windows.flashCardsWindow import FlashCardsWindow
from classes.windows.settingsWindow import SettingsWindow
from classes.database.db import Database
from classes.database.migration import Migration
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

        super().__init__()
        self.initializeUI()
        self.setupUIConfigurators()
        self.bootstrapDatabase()
        self.initializeServices()
        self.setupConnections()

    def initializeUI(self) -> None:
        """
            UI initialization
        """
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my.app.id")
        self.ui.currentTranslator = Translators.GOOGLE

    def setupUIConfigurators(self):
        """
            Setup UI configurators
        """
        
        MainWindowConfigurator(self.ui).apply()
    
    def initializeServices(self) -> None:
        """
            Services initialization
        """
        
        self.styles = Styles(self)
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        self.loadLang = LoadingLangs(self.ui)
        self.menu = Menu(self, self.db)
        self.translationView = TranslationViewWindow(self.ui, self.db)
        self.flashCards = FlashCardsWindow(self.ui, self.db)
        self.settingsWindow = SettingsWindow(self.ui, self.db)
        
    def setupConnections(self) -> None:
        """
            Loading program actions
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
            GoToRouteAction(self.ui.FlashCardsWindow, self.navigator, Routes.FLASHCARDS, self.flashCards.prepareWindow),
            GoToRouteAction(self.ui.SettingsWindow, self.navigator, Routes.SETTINGS, self.settingsWindow.prepareWindow)
        ]

        # Triggers
        self.ui.actionExit.triggered.connect(self.menu.exitProgramm)
        self.ui.chooseTranslator.triggered.connect(self.loadLang.chooseTranslator)

    def bootstrapDatabase(self) -> None:
        """
            Bootstrap Database
        """

        self.db = Database()
        Migration(self.db).createTables()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
