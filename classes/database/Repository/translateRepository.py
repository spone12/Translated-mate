from ..db import Database
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
        except Exception:
            self.logger.exception("Failed to fetch translations")
            raise
        
    
    def insert(self, data: TranslateDTO) -> int:
        """
            Insert data into table
        """
        
        try:
            self.db.cursor.execute("""
                INSERT INTO Translate 
                (source_text, target_text, source_lang, target_lang, translator)
                VALUES (?, ?, ?, ?, ?)
            """, (
                data.source_text,
                data.target_text,
                data.source_lang,
                data.target_lang,
                data.translator
            ))
            
            self.db.commit()
            return self.db.cursor.lastrowid
        except Exception:
            self.logger.exception("Failed to insert into table translations")
            raise
        
    def delete(self, id: int) -> None:
        """
            Delete row from table by ID
        """

        try:
            self.db.cursor.execute('DELETE FROM Translate WHERE id = ?', (id, ))
            self.db.commit()
        except Exception:
            self.logger.exception("Failed to delete row from translations")
            raise
