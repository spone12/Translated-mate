from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class TranslationModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=QModelIndex()):
        """
            Table row count
        """
        
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """
            Table column count
        """
        
        return len(self._headers)

    def data(self, index, role):
        """
            Data
        """

        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[row][col])

        return None

    def headerData(self, section, orientation, role):
        """
            Header data
        """
        
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
        return None

    def getRowId(self, row):
        """
            Get row ID
        """
        
        return self._data[row][0]

    def removeRowById(self, rowId):
        """
            Remove row by ID
        """
        
        for i, row in enumerate(self._data):
            if row[0] == rowId:
                self.beginRemoveRows(QModelIndex(), i, i)
                self._data.pop(i)
                self.endRemoveRows()
                
                return
            