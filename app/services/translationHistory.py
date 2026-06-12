from app.factories.translate.TranslationUIMapper import TranslationUIMapper


class TranslationHistory:
    def __init__(self, ui, translationMapper: TranslationUIMapper):
        self.ui = ui
        self.translationMapper = translationMapper
        
        self.items = []
        self.position = -1

    def add(self, translation) -> None:
        """Add new history item

        Args:
            translation (TranslateDTO): Translation item
        """

        self.items.append(translation)
        self.position = self.lastIndex()
        self.ui.nextTranslate.setEnabled(False)
        
        # If the number of translates is sufficient, turn on the button
        if self.historyCount() > 1:
            self.ui.prevTranslate.setEnabled(True)
        
    def back(self):
        """Previous history item

        Returns:
            _type_: TranslateDTO
        """
        
        if self.position > 0:
            self.position -= 1
            
            if self.position == 0:
                self.ui.prevTranslate.setEnabled(False)
                
            self.translationMapper.fromDTO(
                self.items[self.position]
            )
            self.ui.nextTranslate.setEnabled(True)

            return self.items[self.position]

    def forward(self):
        """Next history item

        Returns:
            _type_: TranslateDTO
        """
        
        if self.position < self.lastIndex():
            self.position += 1
            
            if self.position == self.lastIndex():
                self.ui.nextTranslate.setEnabled(False)
                
            self.translationMapper.fromDTO(
                self.items[self.position]
            )
            self.ui.prevTranslate.setEnabled(True)
            
            return self.items[self.position]

    def historyCount(self) -> int:
        """Get history count

        Returns:
            _type_: int
        """
        return len(self.items)
    
    def lastIndex(self) -> int:
        """Get last index of history count

        Returns:
            _type_: int
        """
        return self.historyCount() - 1
        
    def current(self):
        """Get current history item

        Returns:
            _type_: TranslateDTO
        """
        
        if self.position >= 0:
            return self.items[self.position]

    def getAll(self) -> list:
        """Get all history

        Returns:
            _type_: list
        """
        
        return self.items
