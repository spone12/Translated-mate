from enum import Enum, unique
from pathlib import Path


# Vosk Enums 
@unique
class VoskEnums(Enum):

    URL = "https://alphacephei.com"
    MODELS_URL = URL + "/vosk/models"
    MODELS_DIR = Path("storage/record/models")
    ZIP_PATH = MODELS_DIR / "model.zip"
    VOSK_MODELS_LIST = MODELS_DIR / "vosk_models.json"

    @classmethod
    def values(vosk) -> list:
        """
            Get vosk enums list 
        """
        
        return [v.value for v in vosk]
    
    @classmethod
    def fromValue(cls, value) -> str:
        """
            Get stt from value
        """
        
        for v in cls:
            if v.value == value:
                return v
        raise ValueError(f"Unknown value: {value}")
