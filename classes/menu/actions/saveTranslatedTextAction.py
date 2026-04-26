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
            trans_from = self.ui.fromLang.currentText(),
            trans_to   = self.ui.toLang.currentText(),
            text_from  = self.ui.inputBox.toPlainText(),
            text_to    = self.ui.translateBox.toPlainText(),
            translator = self.ui.currentTranslator.value,
            knowledge  = 1
        )

        self.service.saveTranslation(dto)
