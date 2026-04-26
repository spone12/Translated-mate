from ..db import Database
from classes.logger import Logger
from classes.database.DTO.translateDTO import TranslateDTO
from .baseRepository import BaseRepository


class TranslateRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    def getAll(self) -> list:
        """
            Get all table data
        """
        
        try:
            return self.db.cursor.execute("SELECT * FROM Translate").fetchall()
        except Exception as err:
            self.logger.log(self.__class__.__name__, f"Select error: {err}")
            raise
        
    
    def insert(self, data: TranslateDTO) -> None:
        """
            Insert data into table
        """
        
        self.db.cursor.execute("""
            INSERT INTO Translate 
            (trans_from, trans_to, text_from, text_to, translator, knowledge)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.trans_from,
            data.trans_to,
            data.text_from,
            data.text_to,
            data.translator,
            data.knowledge
        ))
        self.db.commit()
    
    def delete(self, id: int) -> None:
        """
            Delete row from table by ID
        """

        self.db.cursor.execute('DELETE FROM Translate WHERE id = ?', (id, ))
        self.db.commit()
