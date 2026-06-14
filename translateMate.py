import sys
import ctypes
from PyQt6 import QtCore, QtGui, QtWidgets
from ui.ui_main_window import Ui_MainWindow
from app.styles.styles import Styles
from ui.configurators.mainWindowConfigurator import MainWindowConfigurator
from app.enums.Translate.translators import Translators
from app.core.appContext import AppContext
from app.bootstrap.actionLoader import ActionLoader
from app.bootstrap.databaseLoader import DatabaseLoader


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
        self.ui.generalScrollArea.setWidgetResizable(True)
        
        self.setWindowIcon(QtGui.QIcon('appico.ico'))
        
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "my.app.id"
        )
        
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
        self.context = AppContext(self.ui, self.db, self)
        
    def setupConnections(self) -> None:
        """
            Loading program actions
        """
        
        self.actionLoader = ActionLoader(self.context)
        self.actionLoader.bootstrap()

    def bootstrapDatabase(self) -> None:
        """
            Bootstrap Database
        """

        DBLoader = DatabaseLoader()
        self.db = DBLoader.bootstrap()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TranslateMate()
    window.show()
    sys.exit(app.exec())
