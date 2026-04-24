from enum import Enum, unique

# Translators Enum 
@unique
class Translators(Enum):

    GOOGLE = "Google"
    DEEPL = "Deepl"

    @classmethod
    def values(translators) -> list:
        """
            Get translators list 
        """
        
        return [t.value for t in translators]
    
    @classmethod
    def fromValue(cls, value) -> str:
        """
            Get translator from value
        """
        
        for t in cls:
            if t.value == value:
                return t
        raise ValueError(f"Unknown translator: {value}")
    