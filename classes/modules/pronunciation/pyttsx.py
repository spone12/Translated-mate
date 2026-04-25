import pyttsx3
from .pronunciationInterface import PronunciationInterface

class Pyttsx(PronunciationInterface):

    def __init__(self, text):
        self.engine = pyttsx3.init()
        self.text = text
        self.pronounceText()
    
    def pronounceText(self) -> None:
        """
            Pronounce the text by Pyttsx
        """
        
        self.engine.say(
            self.text
        )

        if not self.engine._inLoop:
            self.engine.runAndWait()
