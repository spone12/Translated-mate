from app.DTO.translateDTO import TranslateDTO


class TranslationUIMapper:
    def __init__(self, ui):
        self.ui = ui

    def toDTO(self) -> TranslateDTO:
        """Get DTO translation object

        Returns:
            TranslateDTO: TranslateDTO object
        """
        
        return TranslateDTO(
            source_text = self.ui.inputBox.toPlainText(),
            target_text = self.ui.translateBox.toPlainText(),
            source_lang = self.ui.sourceLangList.currentText(),
            target_lang = self.ui.targetLangList.currentText(),
            translator  = self.ui.currentTranslator.value
        )
        
    def fromDTO(self, dto: TranslateDTO) -> None:
        """Substitution of values of past translations

        Args:
            dto (TranslateDTO)
        """
        
        self.ui.inputBox.setPlainText(dto.source_text)
        self.ui.translateBox.setPlainText(dto.target_text)

        self.ui.sourceLangList.setCurrentText(dto.source_lang)
        self.ui.targetLangList.setCurrentText(dto.target_lang)
