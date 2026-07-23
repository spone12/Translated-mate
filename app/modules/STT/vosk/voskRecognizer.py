import sys
import queue
import json
import os
import sounddevice as sd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
from vosk import Model, KaldiRecognizer
from pathlib import Path


# Audio configuration (Vosk works best at 16kHz/Mono/int16)
SAMPLE_RATE = 16000
# Slightly larger chunk size for stable recognition
CHUNK_SIZE = 4000
CHANNELS = 1
# Path to the Vosk language model folder
MODEL_PATH = "storage/record/models/vosk-model-small-ru-0.22"

class VoskRecognizer(QThread):
    """
        Speech to text
    """
    
    text_signal = pyqtSignal(str, str)
    error_signal = pyqtSignal(str)
    loaded = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_running = False
        self.audio_queue = queue.Queue()
        self.model = None
        self.recognizer = None

    def loadModel(self, path: str):
        """Load model

        Args:
            path (str): path to model
        """
        try:
            self.model = Model(path)

            self.recognizer = KaldiRecognizer(
                self.model,
                SAMPLE_RATE
            )

            self.loaded.emit()
        except Exception as e:
            self.error_signal.emit(str(e))
    
    def run(self):
        """Run trunscribe"""
        
        self.is_running = True
        
        try:
            # Opening the stream in int16 format (Vosk requirement)
            with sd.RawInputStream(
                samplerate=SAMPLE_RATE,
                blocksize=CHUNK_SIZE,
                dtype="int16",
                channels=CHANNELS,
                callback=self.audio_callback,
            ):
                while self.is_running and not self.isInterruptionRequested():
                    try:
                        # Waiting for audio data from the queue
                        audio_bytes = self.audio_queue.get(timeout=0.1)
                        
                        # Passing bytes to the Vosk recognizer
                        if self.recognizer.AcceptWaveform(audio_bytes):
                            
                            # A pause in speech has been triggered — 
                            # the final phrase of the chunk has been received
                            
                            result_json = json.loads(self.recognizer.Result())
                            text = result_json.get("text", "")
                            if text:
                                self.text_signal.emit("final", text)
                        else:
                            # The user is talking right now (intermediate result)
                            partial_json = json.loads(self.recognizer.PartialResult())
                            partial_text = partial_json.get("partial", "")
                            
                            if partial_text:
                                self.text_signal.emit("partial", partial_text)
                        
                    except queue.Empty:
                        continue
                        
        except Exception as e:
            self.error_signal.emit(f"Recognition flow error: {e}")
    
    def audio_callback(self, indata, frames, time, status):
            """Interception of raw bytes from the microphone"""
            
            if status:
                print(f"Audio error: {status}", file=sys.stderr)
                
            # Putting a copy of the bytes in the queue
            self.audio_queue.put(bytes(indata))
            
    def stop(self):
            """Correct completion of the flow"""
            
            self.is_running = False
            self.requestInterruption()
            self.wait()
