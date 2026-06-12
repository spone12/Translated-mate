from .abstractAction import AbstractAction
from app.database.Services.translateService import TranslateService
from app.database.Repository.translateRepository import TranslateRepository
from app.enums.routes import Routes
from app.core.actionRouter import ActionRouter
from app.factories.translate.TranslationUIMapper import TranslationUIMapper


class SaveTranslatedTextAction(AbstractAction):
    def __init__(self, ui, db, actionRouter: ActionRouter, translationMapper: TranslationUIMapper):
        super().__init__()
        self.ui = ui
        self.service = TranslateService(
            TranslateRepository(db)
        )
        self.translationMapper = translationMapper

        # UI subscription
        self.bind()
        self.bindToast(actionRouter, Routes.SAVED)

    def execute(self) -> None:
        """
            Action save translated text to DB
        """

        rowId = self.service.saveTranslation(
            self.translationMapper.toDTO()
        )
        
        if rowId is None:
            return None
        
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
