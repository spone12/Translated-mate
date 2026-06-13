# Save translation window
from app.core.logger import Logger
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton
from .windowInterface import WindowInterface
from app.models.translationModel import TranslationModel
from app.services.translateService import TranslateService
from app.database.Repository.translateRepository import TranslateRepository


class TranslationViewWindow(WindowInterface):
    """
        Translation window
    """

    columnsWidth = [0, 375, 375, 100, 100, 50]
    headerLabels = ['id', 'Native', 'Translate', 'From', 'To', 'Delete']

    def __init__(self, ui, db):
        self.ui = ui
        self.service = TranslateService(
            TranslateRepository(db)
        )
    
    def renderSavedTable(self) -> None:
        """
            Render saved translation table
        """

        data = self.service.getAll()
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
        """ Delete row from table """
        rowId = self.model.getRowId(row)

        self.service.deleteRow(rowId)
        self.model.removeRowById(rowId)

    def prepareWindow(self) -> None:
        """
            Prepare the window "Saved translations"
        """
        
        self.renderSavedTable()
