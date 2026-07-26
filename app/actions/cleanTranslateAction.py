from .abstractAction import AbstractAction


class CleanTranslateAction(AbstractAction):
    def __init__(self, ui, speechService):
        self.ui = ui
        self.speechService = speechService

        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Clean input and translated text
        """
        
        self.speechService.stop()
        self.ui.translateBox.clear()
        self.ui.inputBox.clear()

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.cleanTranslate
