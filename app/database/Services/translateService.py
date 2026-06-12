from ..Repository.translateRepository import TranslateRepository
from app.database.DTO.translateDTO import TranslateDTO


class TranslateService:
    def __init__(self, repo: TranslateRepository):
        self.repo = repo

    def getAll(self) -> list:
        """
            Get all data
        """
        
        return self.repo.getAll()

    def saveTranslation(self, data: TranslateDTO) -> int:
        """
            Service logic Translate table before insert
        """

        if not data.source_text or not data.target_text:
            return None
        
        return self.repo.insert(data)

    def deleteRow(self, id: int) -> None:
        """
            Delete row by ID
        """
        
        self.repo.delete(id)    
