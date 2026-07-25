import json
import requests
from bs4 import BeautifulSoup
from app.enums.STT.vosk import VoskEnums
from app.enums.Translate.translators import Translators
from app.translate.TranslationResources.languages import TRANSLATOR_LANGS


class UpdateModelList():
    """
        Update vosk models list
    """
    
    def __init__(self):
        self.languageCodes = []
    
    def updateList(self) -> bool:
        """Update language vosk models list

        Returns:
            bool: success
        """
        
        response = requests.get(VoskEnums.MODELS_URL.value)
        soup = BeautifulSoup(response.text, "html.parser")

        languages = TRANSLATOR_LANGS[Translators.GOOGLE]
        self.languageCodes = sorted(
            languages.keys(),
            key=len,
            reverse=True
        )

        models = {}

        for link in soup.select("a[href$='.zip']"):

            href = link["href"]
            name = href.split("/")[-1].replace(".zip", "")

            language = self.detectLanguage(name)

            if not language:
                continue

            size = self.detectModelSize(name)
            models.setdefault(language, {})
            
            if size not in models[language]:
                
                models[language][size] = {
                    "name": name,
                    "url": href if href.startswith("http")
                        else f"{VoskEnums.URL.value}{href}"
                }

        # VoskEnums.VOSK_MODELS_LIST.parent.mkdir(
        #     parents=True,
        #     exist_ok=True
        # )
        
        with open(VoskEnums.VOSK_MODELS_LIST.value, "w", encoding="utf-8") as file:
            json.dump(models, file, indent=4, ensure_ascii=False)
        
        return True

    def detectLanguage(self, modelName: str) -> str | None:
        """Detect model language

        Args:
            modelName (str): model name

        Returns:
            str | None: language
        """
        
        for code in self.languageCodes:
            if f"-{code}-" in modelName:
                return code
            
        return None

    def detectModelSize(self, name: str) -> str:
        """Detect model size

        Args:
            name (str): model name

        Returns:
            str: size
        """
        
        if "small" in name:
            return "small"

        return "large"
