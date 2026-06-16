import json
from app.enums.filePaths import FilePaths


class SettingsService:
    
    def __init__(self):
        self._settings = {}

    def get(self, key, default=None):
        """Get settings value by key

        Args:
            key (_type_): _description_
            default (_type_, optional): Set default vakye

        Returns:
            _type_: Value
        """
        return self._settings.get(key, default)
    
    def getAll(self):
        """Get all settings

        Returns:
            _type_: _description_
        """
        return self._settings

    def set(self, key, value):
        """Set settings value

        Args:
            key (_type_): key
            value (_type_): value
        """
        self._settings[key] = value
        self.save()

    def load(self):
        """Load settings
        """
        if not FilePaths.SETTINGS_FILE.value.exists():
            self._settings = {}
            return
        
        with open(FilePaths.SETTINGS_FILE.value, "r", encoding="utf-8") as file:
            self._settings = json.load(file)


    def save(self):
        """Save settings"""
        with open(FilePaths.SETTINGS_FILE.value, "w", encoding="utf-8") as file:
            json.dump(
                self._settings,
                file,
                ensure_ascii=False,
                indent=4
            )
