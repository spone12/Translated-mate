from classes.enums.Translate.translators import Translators
from .googleTranslateLanguages import googleLanguages
from .deeplTranslateLanguages import deeplLanguages

TRANSLATOR_LANGS = {
    Translators.GOOGLE: googleLanguages,
    Translators.DEEPL: deeplLanguages
}
