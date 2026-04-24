from requests.exceptions import HTTPError
from classes.logger import *
from classes.enums.Translate.translators import Translators
from classes.translate.TranslationResources.languages import TRANSLATOR_LANGS


class LoadingLangs():
    """
        Load language
    """

    def __init__(self, ui):
        self.ui = ui
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

        self.ui.fromLang.clear()
        self.ui.toLang.clear()

        self.ui.fromLang.addItems(languageValues)
        self.ui.fromLang.setCurrentIndex(languageValues.index('English'))
        
        self.ui.toLang.addItems(languageValues)
        
        if translator == Translators.GOOGLE:
            self.ui.toLang.model().item(0).setEnabled(False)
            
        self.ui.toLang.setCurrentIndex(languageValues.index('Russian'))

    def getKeyLang(self, value) -> str:
        """
            Get country code by full language name
        """
        
        languagesArray = self.getListTranslatorLanguages().items()
        
        for k, v in languagesArray:
            if (isinstance(v, list) and value in v) or value == v:
                return k
        else:
            Logger().log(self.__class__.__name__, f"Cant find language: {value}")
            return 'auto'

    def getListTranslatorLanguages(self):
        """
            Get a list of translator languages
        """

        return TRANSLATOR_LANGS[self.ui.currentTranslator]
    