from app.core.navigator import Navigator
from app.translate.TranslationResources.loadLangs import LoadingLangs
from app.windows.TranslationViewWindow import TranslationViewWindow
from app.windows.flashCardsWindow import FlashCardsWindow
from app.windows.settingsWindow import SettingsWindow
from app.core.actionRouter import ActionRouter
from app.core.appLifecycle import AppLifecycle


class AppContext:
    def __init__(self, ui, db, window):
        self.ui = ui
        self.db = db
        self.window = window
        
        # Windows
        self.translationView = TranslationViewWindow(self.ui, self.db)
        self.flashCards = FlashCardsWindow(self.ui, self.db)
        self.settingsWindow = SettingsWindow(self.ui)
        
        # Menu
        self.lifecycle = AppLifecycle(self.window, self.db)
        
        #Navigator
        self.navigator = Navigator(self.ui)
        self.navigator.goTo(self.navigator.default)
        
        # Router
        self.actionRouter = ActionRouter()
        
        # Langs
        self.loadLang = LoadingLangs(self.ui)
