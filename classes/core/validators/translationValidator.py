class TranslationValidator:

    def isValid(self, text: str) -> bool:
        """ Check if text valid """
        return bool(text.strip())

    def canSave(self, source: str, target: str) -> bool:
        """ Can save text """
        return self.isValid(source) and self.isValid(target)
