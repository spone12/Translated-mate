# Settings window
from classes.logger import Logger
from .windowInterface import WindowInterface


class SettingsWindow(WindowInterface):
    """
        Flash cards window
    """

    def __init__(self, ui, db):
        self.ui = ui

    def renderSettings(self) -> None:
        """
            Render a settings data
        """
        
        print("Settings")

    def prepareWindow(self) -> None:
        """
            Prepare the window "Settings"
        """
        
        self.renderSettings()
