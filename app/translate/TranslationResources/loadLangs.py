from requests.exceptions import HTTPError
from app.core.logger import Logger
from app.enums.Translate.translators import Translators
from app.services.detector.languageDetector import LanguageDetector
from .languages import TRANSLATOR_LANGS


class LoadingLangs():
    """
        Load language
    """

    def __init__(self, ui):
        self.ui = ui
        self.logger = Logger().getLogger(self.__class__.__name__)
        self.langDetector = LanguageDetector()
        self.loadLangArrays(self.ui.currentTranslator)
        
    def chooseTranslator(self, event):
        """
            Choose the translaor
        """
        if not event.isChecked():
            event.setChecked(True)
            return

        # Remove active translators
        for i in self.ui.chooseTranslator.actions():
            if i.text() != event.text() and i.isChecked():
                i.setChecked(False)

        self.ui.currentTranslator = Translators.fromValue(event.text())
        self.loadLangArrays(event.text())
        
    def loadLangArrays(self, translator = Translators.GOOGLE) -> None:
        """
            Change of translator and loading of language arrays
        """

        languageValues = list(self.getListTranslatorLanguages().values())

        self.ui.sourceLangList.clear()
        self.ui.targetLangList.clear()

        self.ui.sourceLangList.addItems(languageValues)
        self.ui.sourceLangList.setCurrentIndex(languageValues.index('English'))
        
        self.ui.targetLangList.addItems(languageValues)
        
        if translator == Translators.GOOGLE:
            self.ui.targetLangList.model().item(0).setEnabled(False)
            
        self.ui.targetLangList.setCurrentIndex(languageValues.index('Russian'))

    def getKeyLang(self, language: str, text:str = '') -> str:
        """
            Getting the language country code by name
        """
        
        languagesList = self.getListTranslatorLanguages()
        
        # Checking for presence in an array
        for k, llist in languagesList.items():
            if (isinstance(llist, list) and language in llist) or language == llist:
                return k
        else:
            # Language detection
            if text:
                detectedLanguage = self.langDetector.detect(text)
                
                if detectedLanguage in languagesList:
                    return detectedLanguage
                
        return 'auto'

    def getListTranslatorLanguages(self):
        """
            Get a list of translator languages
        """

        return TRANSLATOR_LANGS[self.ui.currentTranslator]
