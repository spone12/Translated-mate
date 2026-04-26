import sqlite3
from classes.logger import Logger

class Database:
    def __init__(self, dbPath: str = "translate.db"):
        self.conn = sqlite3.connect(dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def commit(self) -> None:
        """
            Save changes made during the current transaction to the database
        """
        
        try:
           self.conn.commit()
        except Exception as err:
            Logger().log(self.__class__.__name__, f"Database error: {err}")    
        

    def close(self) -> None:
        """
            Close DB connection and save data
        """

        self.conn.commit()
        self.conn.close()
