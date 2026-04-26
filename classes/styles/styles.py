from pathlib import Path


class Styles:

    extension = "css"

    def __init__(self, ui):
        self.ui = ui
        self.base_path = Path("ui/styles")
        self.files = [
            "MainWindow.css",
            "TranslationTable.css"
        ]

        self.apply()

    def apply(self) -> None:
        """
            Apply styles to window
        """
        styles = ""

        for file in self.files:
            path = self.base_path / file

            with open(path, "r", encoding="utf-8") as f:
                styles += f.read() + "\n"
        
        self.ui.setStyleSheet(styles)
