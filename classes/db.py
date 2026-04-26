# Save translation window
import sqlite3
from classes.logger import Logger


class DB():
    """
        DB class
    """

    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect('translate.db')
        self.curs = self.conn.cursor()
        self.createTranslateTable()

    def createTranslateTable(self) -> None:
        """
            Create translate table IF not exist
        """
        
        self.curs.execute('''
            CREATE TABLE IF NOT EXISTS Translate (
                id INTEGER PRIMARY KEY,
                trans_from TEXT NOT NULL,
                trans_to TEXT NOT NULL,
                text_from TEXT NOT NULL,
                text_to TEXT NOT NULL,
                knowledge SMALLINT DEFAULT 1,
                translator VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    def getSavedTranslate(self, where = None):
        """
            Get saved translated rows
        """

        try:
            sql = "SELECT * FROM Translate"
            
            if where is not None:
                sql += " WHERE " + where

            self.curs.execute(sql)
            return self.curs.fetchall()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Select error: {err}")

    def insertTranslate(self, knowledge = 1) -> None:
        """
            Insert Row
        """

        try:
            self.curs.execute('INSERT INTO Translate (trans_from, trans_to, text_from, text_to, translator, knowledge) VALUES (?, ?, ?, ?, ?, ?)',
                (
                    self.ui.fromLang.currentText(),
                    self.ui.toLang.currentText(),
                    self.ui.inputBox.toPlainText(), 
                    self.ui.translateBox.toPlainText(), 
                    self.ui.currentTranslator.value, 
                    knowledge
                )
            )

            self.conn.commit()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Insert error: {err}")

    def updateTranslate(self, id, text) -> None:
        """
            Update Row
        """

        try:
           self.curs.execute('UPDATE Translate SET text = ? WHERE id = ?', (text, id))
           self.conn.commit()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Update error: {err}")

    def deleteTranslate(self, id) -> None:
        """
            Delete Row
        """

        try:
           self.curs.execute('DELETE FROM Translate WHERE id = ?', (id, ))
           self.conn.commit()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Delete error: {err}")        

    def close(self):
        """
            Close DB connection and save data
        """
        
        self.conn.commit()
        self.conn.close()
