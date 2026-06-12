from app.core.navigator import Navigator
from app.translate.TranslationResources.loadLangs import LoadingLangs
from app.windows.TranslationViewWindow import TranslationViewWindow
from app.windows.flashCardsWindow import FlashCardsWindow
from app.windows.settingsWindow import SettingsWindow
from app.menu.menu import Menu
from app.core.actionRouter import ActionRouter


class AppContext:
    def __init__(self, ui, db, window):
        self.ui = ui
        self.db = db
        self.window = window
        
        #Navigator
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        
        # Langs
        self.loadLang = LoadingLangs(self.ui)
        
        # Menu
        self.menu = Menu(self, self.db)
        
        # Windows
        self.translationView = TranslationViewWindow(self.ui, self.db)
        self.flashCards = FlashCardsWindow(self.ui, self.db)
        self.settingsWindow = SettingsWindow(self.ui, self.db)
        
        # Router
        self.actionRouter = ActionRouter()
