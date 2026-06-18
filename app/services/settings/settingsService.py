import json
from typing import Any
from app.enums.filePaths import FilePaths


class SettingsService:
    
    def __init__(self):
        self._settings = {}

    def get(self, path: str, default: Any = None) -> Any: 
        """Get settings value by key

        Args:
            path (str): The path to the specific setting
            default (mixed, optional): Set default value

        Returns:
            Any: Value
        """
        
        keys = path.split(".")
        value = self._settings
        
        for key in keys:
            if not isinstance(value, dict):
                return default
            
            value = value.get(key)
            
            if value is None:
                return default
            
        return value
    
    def getAll(self) -> list:
        """Get all settings

        Returns:
            list: All settings
        """
        return self._settings

    def set(self, path: str, value: Any) -> None:
        """Set settings value

        Args:
            path (str): The path to the specific setting
            value (mixed): value to set
        """
        
        keys = path.split(".")
        settings = self._settings
        
        for key in keys[:-1]:
            if key not in settings:
                settings[key] = {}
            
            settings = settings[key]
            
        settings[keys[-1]] = value
        self.save()

    def load(self) -> None:
        """Load settings
        """
        if not FilePaths.SETTINGS_FILE.value.exists():
            self._settings = {}
            return
        
        with open(FilePaths.SETTINGS_FILE.value, "r", encoding="utf-8") as file:
            self._settings = json.load(file)


    def save(self) -> None:
        """Save settings"""
        with open(FilePaths.SETTINGS_FILE.value, "w", encoding="utf-8") as file:
            json.dump(
                self._settings,
                file,
                ensure_ascii=False,
                indent=4
            )
