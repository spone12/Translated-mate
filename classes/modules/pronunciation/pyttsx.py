import pyttsx3

class Pyttsx():

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
        self.engine.runAndWait()

