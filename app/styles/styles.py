from app.enums.filePaths import FilePaths


class Styles:

    EXTENSION = ".css"

    def __init__(self, ui):
        self.ui = ui
        self.basePath = FilePaths.STYLES_PATH.value
        self.files = [
            "Main" + self.EXTENSION,
            "Buttons" + self.EXTENSION,
            "TranslationTable" + self.EXTENSION,
            "SettingsWindow" + self.EXTENSION
        ]

        self.apply()

    def apply(self) -> None:
        """
            Apply styles to window
        """
        styles = ""

        for file in self.files:
            path = self.basePath / file

            with open(path, "r", encoding="utf-8") as f:
                styles += f.read() + "\n"
        
        self.ui.setStyleSheet(styles)
