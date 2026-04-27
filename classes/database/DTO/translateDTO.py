from dataclasses import dataclass

@dataclass
class TranslateDTO:
    source_text: str
    target_text: str
    source_lang: str
    target_lang: str
    translator: str
    