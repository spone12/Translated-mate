from app.modules.STT.vosk.voskRecognizer import VoskRecognizer
from pathlib import Path


class MicrophoneService:

    def __init__(self, ui):
        self.ui = ui
        self.audioThread = None
        self.fullTranscript = []

    def start(self, path: Path) -> None:
        """Start voice recognition

        Args:
            path (Path): path to model
        """
        
        self.audioThread = VoskRecognizer()
        self.audioThread.loadModel(path)
        self.audioThread.start()
        
        # Show record Mic Icon
        self.ui.microphone.hide()
        self.ui.offMicrophone.show()

    def stop(self) -> None:
        """Stop signal to record voice"""

        if self.audioThread and self.audioThread.isRunning():
            self.fullTranscript = []
            self.audioThread.stop()
            
            # Disable record Mic Icon
            self.ui.offMicrophone.hide()
            self.ui.microphone.show()

    def transcriptAppend(self, text: str) -> None:
        """Append transcript

        Args:
            text (str): _description_
        """
        
        self.fullTranscript.append(text)
    
    def transcriptGet(self) -> list:
        """Get transcript text

        Returns:
            list: _description_
        """
        
        return self.fullTranscript
