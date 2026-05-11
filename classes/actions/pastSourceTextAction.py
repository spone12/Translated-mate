from PyQt6.QtWidgets import QApplication
from .abstractAction import AbstractAction


class PastSourceTextAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """ Paste text from the clipboard for translate """
        
        app = QApplication([])

        # Get the clipboard object
        clipboard = app.clipboard()

        # Retrieve the clipboard text
        text = clipboard.text()

        print(f"Clipboard contains: {text}")        

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.pastSourceText
