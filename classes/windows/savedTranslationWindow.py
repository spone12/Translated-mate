# Save translation window
from classes.logger import *
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton


class SavedTranslationWindow():
    """
        Translation window
    """

    QSindex = 1
    columnsWidth = [50, 100, 100, 350, 350, 50]
    headerLabels = ['id', 'From', 'To', 'Native', 'Translate', 'Delete']

    def __init__(self, ui):
        self.ui = ui
    
    def renderSavedTable(self) -> None:
        """
            Render a saved translation table
        """

        savedTranslations = self.ui.db.getSavedTranslate()

        # Disable vertical header
        self.ui.savedTranslateWidget.verticalHeader().hide()

        # Set row and columns count
        self.ui.savedTranslateWidget.setRowCount(len(savedTranslations))
        self.ui.savedTranslateWidget.setColumnCount(6)

        # Set name header columns
        self.ui.savedTranslateWidget.setHorizontalHeaderLabels(self.headerLabels)

        # Set column width
        for ind, width in enumerate(self.columnsWidth):
            self.ui.savedTranslateWidget.setColumnWidth(ind, width)

        # Set read-only for name language columns
        delegate = ReadOnlyDelegate(self.ui.savedTranslateWidget)

        # Block system columns edit
        for i in range(0, 3):
            self.ui.savedTranslateWidget.setItemDelegateForColumn(i, delegate)

        # Render table
        rowIndex = 0
        for translation in savedTranslations:
            for j in range (0, 6):
                if j == 5:
                    deleteButton = QPushButton("X")
                    self.ui.savedTranslateWidget.setCellWidget(rowIndex, (j), deleteButton)
                    deleteButton.clicked.connect(self.deleteRow)
                else:
                    self.ui.savedTranslateWidget.setItem(
                        rowIndex, (j), QtWidgets.QTableWidgetItem(str(translation[j]))
                    )
            rowIndex += 1 

    def deleteRow(self):
        """
            Delete Row
        """
        
        button = self.ui.sender()
        if button: 
            row = self.ui.savedTranslateWidget.indexAt(button.pos()).row()
            translateId = int(self.ui.savedTranslateWidget.item(row, 0).text())
            self.ui.savedTranslateWidget.removeRow(row)
            self.ui.db.deleteTranslate(translateId)

    def changeWindow(self) -> None:
        """
            Change the window to "saved translations"
        """
        
        self.renderSavedTable()
        self.ui.stackedWidget.setCurrentIndex(self.QSindex)


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return 
