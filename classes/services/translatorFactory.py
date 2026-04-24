from classes.enums.Translate.translators import Translators
from classes.translate.googleTranslator import GoogleTranslator
from classes.translate.deeplTranslator import DeeplTranslator


class TranslatorFactory:
    def getTranslator(self, translatorType):
        """
            Get translator class by translator type
        """
        
        match translatorType:
            case Translators.GOOGLE:
                return GoogleTranslator()
            case Translators.DEEPL:
                return DeeplTranslator()
            