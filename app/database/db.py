import sqlite3
from app.core.logger import Logger


class Database:
    def __init__(self, dbPath: str = "translate.db"):
        self.conn = sqlite3.connect(dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.logger = Logger().getLogger(self.__class__.__name__)

    def commit(self) -> None:
        """
            Save changes made during the current transaction to the database
        """
        
        try:
            self.conn.commit()
        except Exception:
            self.logger.exception("Database commit failed")
            raise

    def close(self) -> None:
        """
            Close DB connection and save data
        """

        self.conn.commit()
        self.conn.close()
