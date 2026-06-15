from app.services.settings.settingsService import SettingsService
from .generalSettingsController import GeneralSettingsController


class SettingsController:
    def __init__(self, ui):
        self.settings = SettingsService()
        self.general = GeneralSettingsController(ui, self.settings)

    def init(self):
        self.settings.load()
        self.general.load()

        self.general.bind()

    def refresh(self) -> None:
        """
            Refresh a settings data
        """
        
        print("Refresh settings")
