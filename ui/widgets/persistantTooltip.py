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

    def showText(
        self,
        pos,
        text: str,
        duration: int = 2000,
        isError: bool = False
    ) -> None:
        """ Show tooltip text

        Args:
            pos (_type_): _description_
            text (str): _description_
            duration (int, optional): _description_. Defaults to 2000.
            isError (bool, optional): _description_. Defaults to False.
        """
        
        self.setText(text)
        self.adjustSize()
        self.move(pos)
        self.show()

        if isError:
            self.errorMessage()
            
        QTimer.singleShot(duration, self.hide)

    def errorMessage(self) -> None:
        """ Error message """
        
        self.setStyleSheet("""
            background-color: #870832;
            color: white;
            padding: 6px;
            border-radius: 6px;
        """)
