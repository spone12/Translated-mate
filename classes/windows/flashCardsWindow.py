# Save translation window
from classes.logger import *
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton


class FlashCardsWindow():
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
    