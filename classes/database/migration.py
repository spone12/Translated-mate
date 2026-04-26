from .db import Database

class Migration:
    def __init__(self, db: Database):
        self.db = db

    def createTables(self) -> None:
        """
            Create tables migration
        """
        
        self.db.cursor.execute("""
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
        """)

        self.db.commit()
