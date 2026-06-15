class SettingsService:
    def __init__(self):
        self._settings = {}

    def get(self, key, default=None):
        return self._settings.get(key, default)
    
    def getAll(self):
        return self._settings

    def set(self, key, value):
        self._settings[key] = value

    def load(self):
        # later: load settings
        pass

    def save(self):
        # later: save to file
        pass
