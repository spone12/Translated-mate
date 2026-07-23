from app.modules.STT.vosk.voskRecognizer import VoskRecognizer


class MicrophoneService:

    def __init__(self):
        self.audioThread = None
        self.fullTranscript = []

    def start(self, path: str) -> None:
        """_summary_

        Args:
            path (str): path to model
        """
        
        self.audioThread = VoskRecognizer()
        self.audioThread.loadModel(path)
        self.audioThread.start()

    def stop(self) -> None:
        """_summary_
        """

        if self.audioThread and self.audioThread.isRunning():
            self.fullTranscript = []
            self.audioThread.stop()

    def transcriptAppend(self, text: str) -> None:
        """_summary_

        Args:
            text (str): _description_
        """
        
        self.fullTranscript.append(text)
    
    def transcriptGet(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        
        return self.fullTranscript
