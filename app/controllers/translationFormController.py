from app.validators.translationValidator import TranslationValidator


class TranslationFormController:
    def __init__(self, validator: TranslationValidator):
        self.validator = validator

    def getState(self, source: str, target: str) -> list:
        """ Get translate boxes state """

        return {
            "is_valid": self.validator.isValid(source),
            "is_valid_target": self.validator.isValid(target),
            "can_save": self.validator.canSave(source, target),
            "chars": len(source),
            "words": len(source.split())
        }
