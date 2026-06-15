from abc import ABC, abstractmethod

class BaseSettingsController(ABC):
    def __init__(self, ui, settingsService):
        self.ui = ui
        self.settings = settingsService

    @abstractmethod
    def load(self): raise NotImplementedError

    @abstractmethod
    def bind(self): raise NotImplementedError
