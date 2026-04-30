from .abstractAction import AbstractAction

class CleanTranslateAction(AbstractAction):
    def __init__(self, ui):
        self.ui = ui

        # UI subscription
        self.widget.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Clean input and translated text
        """
        
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.cleanTranslate
