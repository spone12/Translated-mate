from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from .abstractAction import AbstractAction


class PastSourceTextAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """ Paste text from the clipboard for translate """

        # Get the clipboard object
        clipboard = QApplication.clipboard()
        # Get mime data
        mime = clipboard.mimeData()

        if mime.hasText() and not mime.hasImage():
            # Clear input box
            self.ui.inputBox.clear()
            
            # Retrieve the clipboard text
            text = mime.text()
            
            # Past text after 500 ms
            QTimer.singleShot(
                500,
                lambda: self.ui.inputBox.insertPlainText(text)
            )

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.pastSourceText
