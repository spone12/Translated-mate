from app.enums.Translate.translators import Translators
from app.translate.googleTranslator import GoogleTranslator
from app.translate.deeplTranslator import DeeplTranslator


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
