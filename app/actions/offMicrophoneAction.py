from .abstractAction import AbstractAction


class OffMicrophoneAction(AbstractAction):
    def __init__(self, ui, speechService):
        self.ui = ui
        self.speechService = speechService
        
        # UI subscription
        self.bind()

    def execute(self) -> None:
        """
            Microphone action
        """
        
        self.speechService.stop()

    @property
    def widget(self):
        """ Get current widget """
        return self.ui.offMicrophone
