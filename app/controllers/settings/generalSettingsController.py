from .baseSettingsController import BaseSettingsController
from app.enums.Translate.translators import Translators


class GeneralSettingsController(BaseSettingsController):
    
    DEFAULT_TRANSLATOR_KEY = "defaultTranslator"
    
    def load(self) -> None:
        """Load General settings"""
        
        self.ui.generalScrollArea.setWidgetResizable(True)
        self.loadDefaultTranslatorComboBox()
        
    def bind(self) -> None:
        """Bind handlers"""
        
        self.ui.defaultTranslatorComboBox.currentIndexChanged.connect(
            self.onChangedTranslator
        )
        
    def loadDefaultTranslatorComboBox(self):
        """Load translator combo box"""
        for translator in Translators:
            self.ui.defaultTranslatorComboBox.addItem(
                translator.name.title(),
                translator
            )

        savedValue = self.settings.get(
            self.DEFAULT_TRANSLATOR_KEY,
            self.settings.get(self.DEFAULT_TRANSLATOR_KEY)
        )

        translator = Translators(savedValue)
        index = self.ui.defaultTranslatorComboBox.findData(translator)

        if index >= 0:
            self.ui.defaultTranslatorComboBox.setCurrentIndex(index)

        # Set current translator
        self.ui.currentTranslator = (
            self.ui.defaultTranslatorComboBox.currentData()
        )
        self.changeRuntimeTranslator(translator)

    def onChangedTranslator(self, index: int) -> None:
        """On changed translator handler

        Args:
            index (int): Combo box index
        """
        
        # Permament setting
        translator = self.ui.defaultTranslatorComboBox.itemData(index)
        self.settings.set(self.DEFAULT_TRANSLATOR_KEY, translator.value)
        self.ui.currentTranslator = translator
        
        # Runtime
        self.changeRuntimeTranslator(translator)

    def changeRuntimeTranslator(self, translator) -> None:
        """ Changing Top Bar Menu runtime selection """
        
        for action in self.ui.chooseTranslator.actions():
            if action.text() == translator.value:
                action.setChecked(True)
            else:
                action.setChecked(False)
