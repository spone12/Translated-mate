class TranslationValidator:
    def isValid(self, text: str) -> bool:
        """ Check is text valid """
        return bool(text.strip())
