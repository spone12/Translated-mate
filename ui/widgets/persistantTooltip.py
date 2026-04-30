from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QLabel

class PersistentTooltip(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(
            Qt.WindowType.ToolTip
        )

        self.setStyleSheet("""
            background-color: #036d33;
            color: white;
            padding: 6px;
            border-radius: 6px;
        """)

    def showText(self, pos, text: str, duration: int = 2000):
        """ Show tooltip text """
        self.setText(text)
        self.adjustSize()
        self.move(pos)
        self.show()

        QTimer.singleShot(duration, self.hide)
