from enum import Enum, unique

# Window Index Mapping Routes
@unique
class Routes(Enum):

    TRANSLATE = 0
    SAVED = 1
    FLASHCARDS = 2
    SETTINGS = 3
    
    @classmethod
    def values(routes) -> list:
        """
            Get routes indexes 
        """
        
        return [r.value for r in routes]
    