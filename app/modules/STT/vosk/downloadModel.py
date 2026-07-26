import os
import zipfile
import requests
import json
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal
from app.enums.STT.vosk import VoskEnums
from .updateModelList import UpdateModelList


class DownloadModel(QThread):

    download_started = pyqtSignal()
    progress = pyqtSignal(int, str)
    finished = pyqtSignal(Path)
    error = pyqtSignal(str)
    
    def __init__(self, lang: str, fullNameLanguage: str):
        super().__init__()
        self.lang = lang
        self.langFull = fullNameLanguage
        self.models = {}
        self.modelType = "small"
    
    def run(self):
        """Run download model"""
        
        try:
            modelPath = self.download()
            self.finished.emit(modelPath)
        except Exception as e:
            self.error.emit(str(e))
        
    def download(self) -> Path:
        """Download model

        Returns:
            str: model path
        """

        # Donwload list of models
        if not VoskEnums.VOSK_MODELS_LIST.value.exists():
            updateModelsList = UpdateModelList()
            updateModelsList.updateList()
        
        # Check if lang model exists
        with open(VoskEnums.VOSK_MODELS_LIST.value, "r", encoding = "utf-8") as file:
            self.models = json.load(file)
            self.model = self.models.get(self.lang, {}).get(self.modelType, {})

            if self.model.get("url") is None:
                raise Exception(f"Language \"{self.langFull}\" is not supported by Vosk")

        # Output of a ready-made speech recognition model path
        modelPath = VoskEnums.MODELS_DIR.value / self.model.get("name")

        if modelPath.exists():
            return modelPath
        
        # Start downloading model
        self.download_started.emit()
        
        VoskEnums.MODELS_DIR.value.mkdir(
            parents=True,
            exist_ok=True
        )

        response = requests.get(
            self.model.get("url"),
            stream=True,
            timeout=30
        )
        response.raise_for_status()

        total = int(response.headers.get("content-length", 0))
        downloaded = 0

        with open(VoskEnums.ZIP_PATH.value, "wb") as file:
            for chunk in response.iter_content(128 * 1024):

                file.write(chunk)
                downloaded += len(chunk)
                
                downloaded_mb = downloaded / 1024 / 1024
                total_mb = total / 1024 / 1024

                percent = downloaded * 100 / total
                text = f"Downloading model: {downloaded_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)"

                self.progress.emit(int(percent), text)

        try:
            with zipfile.ZipFile(VoskEnums.ZIP_PATH.value) as zipFile:
                if zipFile.testzip():
                    raise Exception("Archive is corrupted")
                
                zipFile.extractall(VoskEnums.MODELS_DIR.value)
        finally:
            # Delete downloaded model zip file
            VoskEnums.ZIP_PATH.value.unlink(missing_ok=True)
        
        return modelPath
