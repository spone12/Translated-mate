from .db import Database

class Migration:
    def __init__(self, db: Database):
        self.db = db

    def createTables(self) -> None:
        """
            Create tables migration
        """
        
        self.db.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Translate (
                id INTEGER PRIMARY KEY,

                source_text TEXT NOT NULL, -- Source text
                target_text TEXT NOT NULL, -- Target text
                
                source_lang TEXT NOT NULL, -- Source language
                target_lang TEXT NOT NULL, -- Target language
                
                translator VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                
                CHECK (source_lang != target_lang)
            );
            
            CREATE TABLE IF NOT EXISTS Dictionary (
                id INTEGER PRIMARY KEY,
                translation_id INTEGER, -- Link to the Translate table if added from the translator
                sentence_id INTEGER NULL, -- For future reference, adding example sentences
                photo TEXT, -- Photo path

                source_word TEXT NOT NULL, -- Word
                target_word TEXT NOT NULL, -- Target word

                source_lang VARCHAR(50) NOT NULL, -- Source word's language
                target_lang VARCHAR(50) NOT NULL, -- Target word's language               

                knowledge SMALLINT NOT NULL DEFAULT 1, -- Knowledge of the word
                last_reviewed_at TIMESTAMP, -- Last review at
                next_review_at TIMESTAMP, -- Next review at
                review_count INTEGER DEFAULT 0, -- Review count
                
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date create
                
                FOREIGN KEY (translation_id) REFERENCES translations(id) ON DELETE SET NULL,
                CHECK (knowledge BETWEEN 1 AND 5),
                CHECK (source_lang != target_lang),
                UNIQUE(source_word, target_word, source_lang, target_lang)
            );
            
            CREATE INDEX IF NOT EXISTS idx_translations_source 
                ON Translate(source_text, target_text);
        """)

        self.db.commit()
