from app.services.settings.settingsService import SettingsService
from .generalSettingsController import GeneralSettingsController
from .translateSettingsController import TranslateSettingsController


class SettingsController:
    def __init__(self, ui):
        self.settings = SettingsService()
        self.generalController = GeneralSettingsController(ui, self.settings)
        self.translateController = TranslateSettingsController(ui, self.settings)

    def init(self):
        self.settings.load()
        
        self.generalController.load()
        self.generalController.bind()
        
        self.translateController.load()
        self.translateController.bind()
        
    def refresh(self) -> None:
        """
            Refresh a settings data
        """
        
        print("Refresh settings")
