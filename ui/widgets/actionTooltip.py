from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer, pyqtSignal


class ActionTooltip(QWidget):
    clicked = pyqtSignal()  # The signal for the transition

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.ToolTip)

        layout = QHBoxLayout(self)

        self.label = QLabel()
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.label.setOpenExternalLinks(False)

        # Catch a click on the link
        self.label.linkActivated.connect(self.clicked.emit)

        layout.addWidget(self.label)

        self.setStyleSheet("""
            background-color: #2b2b2b;
            color: white;
            padding: 8px;
            border-radius: 6px;
        """)

    def calculateToastPosition(self, parent, widget, margin=30, bottom_widget=None):
        """ Calculate toast position """
        parentRect = parent.rect()
        globalPos = parent.mapToGlobal(parentRect.bottomRight())

        bottomOffset = bottom_widget.height() if bottom_widget else 0

        x = globalPos.x() - widget.width() - (margin + 20)
        y = globalPos.y() - widget.height() - (margin) - bottomOffset

        return x, y

    def showText(self, text: str, parent, duration: int = 3000):
        """ Show the toast text message """
        
        self.label.setText(text)
        self.adjustSize()

        x, y = self.calculateToastPosition(parent, self)
        self.move(x, y)

        self.show()
        self.raise_()

        QTimer.singleShot(duration, self.hide)
