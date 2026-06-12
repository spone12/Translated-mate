from app.database.db import Database
from app.database.migration import Migration

class DatabaseLoader:
    def __init__(self):
        self.db = Database()
        
    def bootstrap(self) -> Database:
        """Load database
        """
        
        Migration(self.db).createTables()
        return self.db
