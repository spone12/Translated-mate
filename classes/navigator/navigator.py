
class Navigator:
    def __init__(self, ui):
        self.ui = ui

        self.windows = {
            0: ui.translateWindow,
            1: ui.saveTranslationWindow,
            2: ui.flashCardsWindow
        }

        self.initWindowButtons()

    def initWindowButtons(self) -> None:
        """
           Initializing the Window Buttons property 
        """
        
        for w in self.windows.values():
            w.setProperty("navButton", True)

    def goTo(self, index) -> None:
        """
            Go to another window
        """
        
        # Deselecting window icons
        for w in self.windows.values():
            w.setStyleSheet("")
            w.setProperty("winButton", True)
            w.setProperty("active", False)
            w.style().unpolish(w)
            w.style().polish(w)

        # Setting the selection of the selected window
        current = self.windows[index]
        current.setProperty("active", True)
        current.style().unpolish(current)
        current.style().polish(current)

        self.ui.stackedWidget.setCurrentIndex(index)
