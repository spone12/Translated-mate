from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal(object)

    def mousePressEvent(self, event):
        """
            Mouse press event
        """
        
        self.clicked.emit(event)
        super().mousePressEvent(event)
