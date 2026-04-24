from classes.enums.routes import Routes

class Navigator:
    def __init__(self, ui, defaultWindow = Routes.TRANSLATE):
        self.ui = ui
        self.default = defaultWindow
        self.beforeRoutes = {}

        self.windows = {
            Routes.TRANSLATE: ui.translateWindow,
            Routes.SAVED: ui.saveTranslationWindow,
            Routes.FLASHCARDS: ui.flashCardsWindow
        }

        self.initNavigationButtons()

    def register(self, index, beforeAction=None) -> None:
        """
            Registering routes with actions
        """
    
        self.beforeRoutes[index] = beforeAction

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

        action = self.beforeRoutes.get(index)
        
        # Perform an action if a route is found        
        if action:
            action()

        # Switch page
        self.ui.stackedWidget.setCurrentIndex(index.value)
