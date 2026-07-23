import os
import zipfile
import requests
from PyQt6.QtCore import QThread, pyqtSignal
from pathlib import Path


MODEL_URL = "https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip"
MODEL_DIR = "storage/record/models"
MODEL_PATH = MODEL_DIR + "/vosk-model-small-ru-0.22"
ZIP_PATH = MODEL_DIR + "/model.zip"

class DownloadModel(QThread):

    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        """Run download model"""
        
        try:
            model_path = self.download()
            print(model_path)
            self.finished.emit(model_path)
        except Exception as e:
            self.error.emit(str(e))
        
    def download(self) -> str:
        """Download model

        Returns:
            str: model path
        """
        
        if os.path.exists(MODEL_PATH):
            return MODEL_PATH

        os.makedirs(MODEL_DIR, exist_ok=True)

        response = requests.get(
            MODEL_URL,
            stream=True
        )

        total = int(response.headers["content-length"])
        downloaded = 0

        with open(ZIP_PATH, "wb") as file:

            for chunk in response.iter_content(1024 * 1024):
                print(f"Downloading model: {downloaded}/{total} bytes")
                file.write(chunk)
                downloaded += len(chunk)

                percent = int(downloaded * 100 / total)
                self.progress.emit(percent)

        with zipfile.ZipFile(ZIP_PATH) as zip_file:
            zip_file.extractall(MODEL_DIR)

        # Delete model zip file
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)
            
        return MODEL_PATH
