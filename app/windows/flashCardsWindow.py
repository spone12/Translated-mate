# Save translation window
from app.logger import Logger
from .windowInterface import WindowInterface
from app.database.Services.translateService import TranslateService
from app.database.Repository.translateRepository import TranslateRepository


class FlashCardsWindow(WindowInterface):
    """
        Flash cards window
    """

    def __init__(self, ui, db):
        self.ui = ui
        self.service = TranslateService(
            TranslateRepository(db)
        )

    def renderFlashCards(self) -> None:
        """
            Render a flash cards
        """
        
        savedTranslations = self.service.getAll()
        
        for translation in savedTranslations:
            pass 

    def prepareWindow(self) -> None:
        """
            Prepare the window "Flash cards"
        """
        
        self.renderFlashCards()
