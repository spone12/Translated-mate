# Save translation window
from classes.logger import *
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton
from .windowInterface import WindowInterface
from classes.models.translationModel import TranslationModel


class TranslationViewWindow(WindowInterface):
    """
        Translation window
    """

    columnsWidth = [0, 100, 100, 375, 375, 50]
    headerLabels = ['id', 'From', 'To', 'Native', 'Translate', 'Delete']

    def __init__(self, ui, db):
        self.ui = ui
        self.db = db
    
    def renderSavedTable(self) -> None:
        """
            Render saved translation table
        """

        data = self.db.getSavedTranslate()
        self.model = TranslationModel(data, self.headerLabels)

        table = self.ui.TranslationTableWidget
        table.setModel(self.model)

        # Hide row ID
        table.setColumnHidden(0, True)

        # Set columns width
        for i, width in enumerate(self.columnsWidth):
            table.setColumnWidth(i, width)

        table.setAlternatingRowColors(True)
        table.setShowGrid(False)

        # Render delete button
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 5)

            button = QPushButton("🗑")
            button.setStyleSheet("""
                QPushButton {
                    border: none;
                    font-size: 16px;
                }
                QPushButton:hover {
                    color: red;
                }
            """)

            button.clicked.connect(lambda _, r=row: self.deleteRow(r))
            self.ui.TranslationTableWidget.setIndexWidget(index, button)

    def deleteRow(self, row):
        row_id = self.model.getRowId(row)

        self.db.deleteTranslate(row_id)
        self.model.removeRowById(row_id)

    def prepareWindow(self) -> None:
        """
            Prepare the window "Saved translations"
        """
        
        self.renderSavedTable()
