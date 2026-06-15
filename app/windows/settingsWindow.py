# Settings window
from app.core.logger import Logger
from .windowInterface import WindowInterface
from app.controllers.settings.settingsController import SettingsController


class SettingsWindow(WindowInterface):
    """
        Flash cards window
    """

    def __init__(self, ui):
        self.ui = ui
        
        self.controller = SettingsController(self.ui)
        self.controller.init()

    def prepareWindow(self) -> None:
        """
            Prepare the window "Settings"
        """
        self.controller.refresh()
