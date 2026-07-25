import queue
import json
import sounddevice as sd
from PyQt6.QtCore import QThread, pyqtSignal
from vosk import Model, KaldiRecognizer
from pathlib import Path
from app.core.logger import Logger


class VoskRecognizer(QThread):
    """
        Vosk speach recognizer
    """
    
    # Audio configuration (Vosk works best at 16kHz/Mono/int16)
    SAMPLE_RATE = 16000
    # Slightly larger chunk size for stable recognition
    CHUNK_SIZE = 4000
    CHANNELS = 1

    text_signal = pyqtSignal(str, str)
    error_signal = pyqtSignal(str)
    loaded = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_running = False
        self.audioQueue = queue.Queue()
        self.model = None
        self.recognizer = None
        self.logger = Logger().getLogger(self.__class__.__name__)

    def loadModel(self, path: str) -> None:
        """Load Vosk model

        Args:
            path (str): Path to model
        """
        try:
            self.model = Model(path)

            self.recognizer = KaldiRecognizer(
                self.model,
                self.SAMPLE_RATE
            )

            self.loaded.emit()
        except Exception as e:
            self.error_signal.emit(str(e))
    
    def run(self) -> None:
        """Run trunscribe"""
        
        self.is_running = True
        
        try:
            # Opening the stream in int16 format (Vosk requirement)
            with sd.RawInputStream(
                samplerate = self.SAMPLE_RATE,
                blocksize  = self.CHUNK_SIZE,
                dtype      = "int16",
                channels   = self.CHANNELS,
                callback   = self.audioCallback,
            ):
                while self.is_running and not self.isInterruptionRequested():
                    try:
                        # Waiting for audio data from the queue
                        audioBytes = self.audioQueue.get(timeout = 0.1)
                        
                        # Passing bytes to the Vosk recognizer
                        if self.recognizer.AcceptWaveform(audioBytes):
                            
                            # A pause in speech has been triggered — 
                            # the final phrase of the chunk has been received
                            
                            resultJson = json.loads(self.recognizer.Result())
                            text = resultJson.get("text", "")
                            if text:
                                self.text_signal.emit("final", text)
                        else:
                            # The user is talking right now (intermediate result)
                            partialJson = json.loads(self.recognizer.PartialResult())
                            partialText = partialJson.get("partial", "")
                            
                            if partialText:
                                self.text_signal.emit("partial", partialText)
                        
                    except queue.Empty:
                        continue
                        
        except Exception as e:
            self.error_signal.emit(f"Recognition flow error: {e}")
    
    def audioCallback(self, indata, frames, time, status) -> None:
        """Interception of raw bytes from the microphone

        Args:
            indata (_type_): In data
            frames (_type_): Frames
            time (_type_): Time
            status (_type_): Status
        """
            
        if status:
            self.logger.exception(f"Vosk Audio error: {status}")
            
        # Putting a copy of the bytes in the queue
        self.audioQueue.put(bytes(indata))
            
    def stop(self) -> None:
            """Correct completion of the flow"""
            
            self.is_running = False
            self.requestInterruption()
            self.wait()
