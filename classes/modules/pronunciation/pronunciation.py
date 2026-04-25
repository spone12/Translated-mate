from classes.modules.pronunciation.pyttsx import Pyttsx


class Pronunciation():
    """
        Text pronunciation
    """

    def __init__(self, text):
        self.choisePronunciationModel(text)
    
    def choisePronunciationModel(self, text):
        """
            Choise pronunciation model
        """

        Pyttsx(text)
