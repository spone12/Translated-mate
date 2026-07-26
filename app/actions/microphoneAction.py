from .abstractAction import AbstractAction
from app.modules.STT.vosk.downloadModel import DownloadModel


class MicrophoneAction(AbstractAction):
    def __init__(self, ui, speechService, loadLang):
        self.ui = ui
        self.speechService = speechService
        self.loadLang = loadLang
        self.currentLang = ""
        
        # UI subscription
        self.bind()
        
    def execute(self) -> None:
        """
            Microphone action
        """
        
        self.ui.progressBar.setValue(0)
        currentLangFull = self.ui.sourceLangList.currentText()
        currentLang = self.loadLang.getKeyLang(currentLangFull)

        self.downloader = DownloadModel(currentLang, currentLangFull)
        self.downloader.download_started.connect(self.startDownload)
        self.downloader.progress.connect(self.updateDownloadProgress)
        self.downloader.finished.connect(self.onModelDownloaded)
        self.downloader.error.connect(self.handleError)
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
            path (Path): path to model
        """
        
        self.ui.progressBar.hide()
        self.ui.translateBox.clear()
        
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
            self.refreshTextDisplay(partialText = text)
        
    def refreshTextDisplay(self, partialText: str = "") -> None:
        """Redraws the text, separating the stable text and 
        what is being written right now
        
        Args:
            partialText (str): partial transcribed text
        """
        
        history = " ".join(self.speechService.transcriptGet())
        
        if partialText:
            current_display = f"{history} {partialText}..."
        else:
            current_display = history
        
        #self.ui.inputBox.setHtml(current_display)
        self.ui.inputBox.setPlainText(current_display)
        
        # Automatic scrolling down to new words
        scrollbar = self.ui.inputBox.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def handleError(self, errorMessage: str) -> None:
        """Handle error
        
        Args:
            error_message (str): error
        """
        
        self.speechService.stop()
        self.ui.progressBar.hide()
        
        self.showTooltip(errorMessage, 4000, True)
    
    @property
    def widget(self):
        """ Get current widget """
        return self.ui.microphone
