from enum import Enum, unique
from pathlib import Path


# File paths
@unique
class FilePaths(Enum):

    SETTINGS_FILE = Path("app/config/settings.json")
    STYLES_PATH = Path("ui/styles")
    
    @classmethod
    def values(files) -> list:
        """
            Get files path list
        """
        
        return [f.value for f in files]
