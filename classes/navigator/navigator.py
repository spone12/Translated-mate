
class Navigator:
    def __init__(self, ui, defaultWindow = 0):
        self.ui = ui
        self.default = defaultWindow

        self.windows = {
            0: ui.translateWindow,
            1: ui.saveTranslationWindow,
            2: ui.flashCardsWindow
        }

        self.initNavigationButtons()

    def initNavigationButtons(self) -> None:
        """
           Initializing the navigation buttons property 
        """
        
        for w in self.windows.values():
            w.setProperty("navButton", "true")
            w.setProperty("active", "false")

    def goTo(self, index) -> None:
        """
            Switch to another window
        """
        
        # Reset state
        for w in self.windows.values():
            w.setProperty("active", "false")
            w.style().unpolish(w)
            w.style().polish(w)

        # Set active
        current = self.windows[index]
        current.setProperty("active", "true")
        current.style().unpolish(current)
        current.style().polish(current)

        # Switch page
        self.ui.stackedWidget.setCurrentIndex(index)
