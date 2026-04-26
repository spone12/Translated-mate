# Save translation window
from classes.logger import Logger
from .windowInterface import WindowInterface
from classes.database.Services.translateService import TranslateService
from classes.database.Repository.translateRepository import TranslateRepository


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
            Prepare the window "flash cards"
        """
        
        self.renderFlashCards()
    