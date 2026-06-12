from enum import Enum, unique
from .translators import Translators


# Translators limit Enum 
@unique
class TranslatorsLimit(Enum):

    GOOGLE_LIMIT = (Translators.GOOGLE.value, 10000)
    DEEPL_LIMIT = (Translators.DEEPL.value, 1500)

    @classmethod
    def values(limits) -> list:
        """
            Get translators limits list 
        """
        
        return [l.value for l in limits]

    @classmethod
    def fromValue(cls, value: Translators) -> int:
        """
            Get translator limit by translator name
        """
        
        for item in cls:
            translator_name, limit = item.value

            if translator_name == value.value:
                return limit

        raise ValueError(f"Limit not found for {value}")
