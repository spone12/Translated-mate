from .abstractUIConfigurator import AbstractUIConfigurator

class MainWindowConfigurator(AbstractUIConfigurator):
    def __init__(self, ui):
        self.ui = ui

    def setupUiProperties(self):
        """ Setup UI properties """
        
        elements = (
            self.ui.microphone,
            self.ui.sourcePronunciation,
            self.ui.sourceCopyTranslate,
            self.ui.pronunciation,
            self.ui.copyTranslate,
            self.ui.saveTranslatedText
        )
        
        for elem in elements:
            self.setProperty(elem, "translateButton")
        