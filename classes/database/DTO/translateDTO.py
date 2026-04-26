from dataclasses import dataclass

@dataclass
class TranslateDTO:
    trans_from: str
    trans_to: str
    text_from: str
    text_to: str
    translator: str
    knowledge: int
    