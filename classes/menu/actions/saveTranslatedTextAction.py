from classes.menu.actions.actionInterface import ActionInterface
from classes.database.Services.translateService import TranslateService
from classes.database.Repository.translateRepository import TranslateRepository
from classes.database.DTO.translateDTO import TranslateDTO


class SaveTranslatedTextAction(ActionInterface):
    def __init__(self, ui, db):
        self.ui = ui
        self.service = TranslateService(
            TranslateRepository(db)
        )

        # UI subscription
        self.ui.saveTranslatedText.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Action save translated text to DB
        """

        dto = TranslateDTO(
            source_text = self.ui.inputBox.toPlainText(),
            target_text = self.ui.translateBox.toPlainText(),
            source_lang = self.ui.sourceLangList.currentText(),
            target_lang = self.ui.targetLangList.currentText(),
            translator  = self.ui.currentTranslator.value
        )

        self.service.saveTranslation(dto)
