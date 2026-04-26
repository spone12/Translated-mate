from ..Repository.translateRepository import TranslateRepository
from classes.database.DTO.translateDTO import TranslateDTO

class TranslateService:
    def __init__(self, repo: TranslateRepository):
        self.repo = repo

    def getAll(self) -> list:
        """
            Get all data
        """
        
        return self.repo.getAll()

    def saveTranslation(self, data: TranslateDTO) -> None:
        """
            Service logic Translate table before insert
        """

        if not data.text_to and not data.text_from:
            return None
        
        self.repo.insert(data)

    def deleteRow(self, id: int) -> None:
        """
            Delete row by ID
        """
        
        self.repo.delete(id)    
