from .abstractAction import AbstractAction
from app.modules.STT.vosk.downloadModel import DownloadModel


class MicrophoneAction(AbstractAction):
    def __init__(self, ui, speechService):
        self.ui = ui
        self.speechService = speechService
        
        # UI subscription
        self.bind()
        
    def execute(self) -> None:
        """
            Microphone action
        """
        
        self.ui.progressBar.setValue(0)
        
        self.downloader = DownloadModel()
        self.downloader.download_started.connect(self.startDownload)
        self.downloader.progress.connect(self.updateDownloadProgress)
        self.downloader.finished.connect(self.onModelDownloaded)
        self.downloader.start()
    
    def startDownload(self):
        self.ui.progressBar.setFormat("Downloading model... %p%")
        self.ui.progressBar.show()
    
    def updateDownloadProgress(self, value: int, text: str):
        """Update progress bar

        Args:
            value (int): progress value
            text (str): progress format
        """
        
        self.ui.progressBar.setValue(value)
        self.ui.progressBar.setFormat(text)
    
    def onModelDownloaded(self, path):
        """_summary_
        
        Args:
            path (_type_): _description_
        """
        
        self.ui.progressBar.hide()
        
        # Mic Icons
        self.ui.microphone.hide()
        self.ui.offMicrophone.show()
        
        self.speechService.start(path)
        self.speechService.audioThread.text_signal.connect(
            self.handleTextInput
        )
        self.speechService.audioThread.error_signal.connect(
            self.handleError
        )
    
    def handleTextInput(self, text_type: str, text: str) -> None:
        """Real-time text display
        
        Args:
            text_type (str): signal type
            text (str): transcribed text
        """
        
        if text_type == "final":
            # Saving the finished phrase in the history
            self.speechService.transcriptAppend(text)
            self.refreshTextDisplay()
        elif text_type == "partial":
            # Temporarily output the current unfinished word to the end
            self.refreshTextDisplay(partial_text=text)
        
    def refreshTextDisplay(self, partial_text: str = "") -> None:
        """Redraws the text, separating the stable text and 
        what is being written right now
        
        Args:
            partial_text (str): partial typtranscribed texte
        """
        
        history = " ".join(self.speechService.transcriptGet())
        
        if partial_text:
            current_display = f"{history} {partial_text}..."
        else:
            current_display = history
        
        #self.ui.inputBox.setHtml(current_display)
        self.ui.inputBox.setPlainText(current_display)
        
        # Automatic scrolling down to new words
        scrollbar = self.ui.inputBox.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def handleError(self, error_message:str):
        """Handle error
        
        Args:
            error_message (str): error
        """
        
        self.ui.inputBox.append(f"<br><span style='color: red;'><b>Ошибка:</b> {error_message}</span>")
        self.speechService.stop()
        self.ui.progressBar.hide()
    
    @property
    def widget(self):
        """ Get current widget """
        return self.ui.microphone
