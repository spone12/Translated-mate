from lingua import Language, LanguageDetectorBuilder


class LanguageDetector:
    def __init__(self):
        self.detector = (
            LanguageDetectorBuilder
            .from_all_spoken_languages()
            .build()
        )

    def detect(self, text: str) -> str | None:
        """Language detection

        Args:
            text (str): source text

        Returns:
            str | None: Get language name
        """
        language = self.detector.detect_language_of(text)

        if language is None:
            return None

        return language.iso_code_639_1.name.lower()
