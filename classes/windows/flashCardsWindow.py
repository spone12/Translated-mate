# Save translation window
from classes.logger import Logger
from .windowInterface import WindowInterface


class FlashCardsWindow(WindowInterface):
    """
        Flash cards window
    """

    def __init__(self, ui, db):
        self.ui = ui
        self.db = db

    def renderFlashCards(self) -> None:
        """
            Render a flash cards
        """
        
        savedTranslations = self.db.getSavedTranslate()

        for translation in savedTranslations:
           pass 

    def prepareWindow(self) -> None:
        """
            Prepare the window "flash cards"
        """
        
        self.renderFlashCards()
    