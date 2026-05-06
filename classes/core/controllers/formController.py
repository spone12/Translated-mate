class FormController:
    def __init__(self, validator):
        self.validator = validator

    def getState(self, text: str) -> list:
        """ Get state """

        textLength = len(text)
        return {
            "is_valid": self.validator.isValid(text),
            "can_save": textLength >= 2,
            "length": textLength
        }
