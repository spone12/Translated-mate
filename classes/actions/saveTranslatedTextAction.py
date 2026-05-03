from .abstractAction import AbstractAction
from classes.database.Services.translateService import TranslateService
from classes.database.Repository.translateRepository import TranslateRepository
from classes.database.DTO.translateDTO import TranslateDTO
from classes.enums.routes import Routes
from classes.core.actionRouter import ActionRouter


class SaveTranslatedTextAction(AbstractAction):
    def __init__(self, ui, db, actionRouter: ActionRouter):
        super().__init__()
        self.ui = ui
        self.service = TranslateService(
            TranslateRepository(db)
        )

        # UI subscription
        self.bind()
        self.bindToast(actionRouter, Routes.SAVED)

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
        
        text = '''Translation added to 
        <b style="font-size: 14px; color: orange;">Saved translations</b>
        <br/>
        <a href="#">Open</a>'''
        self.getToast().showText(
            text,
            self.ui.DisplayArea,
            5000
        )

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.saveTranslatedText
