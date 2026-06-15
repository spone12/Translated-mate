from .baseSettingsController import BaseSettingsController
from app.enums.Translate.translators import Translators


class GeneralSettingsController(BaseSettingsController):

    def load(self):

        for translator in Translators:
            self.ui.defaultTranslatorComboBox.addItem(
                translator.name.title(),
                translator
            )

        savedValue = self.settings.get(
            "defaultTranslator",
            Translators.GOOGLE.value
        )

        translator = Translators(savedValue)
        index = self.ui.defaultTranslatorComboBox.findData(translator)

        if index >= 0:
            self.ui.defaultTranslatorComboBox.setCurrentIndex(index)

        # Set current translator
        self.ui.currentTranslator = (
            self.ui.defaultTranslatorComboBox.currentData()
        )
        

    def bind(self):     
        self.ui.defaultTranslatorComboBox.currentTextChanged.connect(
            self.onChanged
        )

    def onChanged(self, value):
        self.settings.set("defaultTranslator", value)
