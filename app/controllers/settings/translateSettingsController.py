from PyQt6.QtGui import QFont 
from .baseSettingsController import BaseSettingsController


class TranslateSettingsController(BaseSettingsController):
    
    TRANSLATE_FONT_SIZE = "translate.fontSize"
    
    def load(self):
        """Load translate settings"""
        self.ui.translateScrollArea.setWidgetResizable(True)
        
        self.loadTranslateFontSizeComboBox()

    def bind(self):
        """Bind handlers"""
        
        self.ui.translateFontSizeComboBox.currentIndexChanged.connect(
            self.onChangedFontSizeBox
        )
    
    def loadTranslateFontSizeComboBox(self):
        """Load translate font size combo box"""
        
        FONT_SIZES = [
            8, 9, 10, 11, 12,
            14, 16, 18, 20,
            24, 28, 32
        ]
        
        for size in FONT_SIZES:
            self.ui.translateFontSizeComboBox.addItem(str(size), size)
        
        index = self.ui.translateFontSizeComboBox.findData(
            self.settings.get(self.TRANSLATE_FONT_SIZE, 16)
        )

        if index >= 0:
            self.ui.translateFontSizeComboBox.setCurrentIndex(index)
            self.applyFontSize(index)

    def onChangedFontSizeBox(self, index: int) -> None:
        """On changed translate font size box handler

        Args:
            index (int): Combo box index
        """
        
        self.settings.set(
            self.TRANSLATE_FONT_SIZE,
            self.ui.translateFontSizeComboBox.itemData(index)
        )
        self.applyFontSize(index)
        
    def applyFontSize(self, index: int) -> None:
        """Apply font size

        Args:
            index (int): index of combo box
        """
        fontSize = self.ui.translateFontSizeComboBox.itemData(index)
        for box in (
            self.ui.inputBox,
            self.ui.translateBox
        ):
            font = QFont()
            font.setPointSize(fontSize)
            box.setFont(font)
