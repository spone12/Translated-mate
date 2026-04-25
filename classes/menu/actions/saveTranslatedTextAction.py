from classes.menu.actions.actionInterface import ActionInterface


class SaveTranslatedTextAction(ActionInterface):
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db

        # UI subscription
        self.ui.saveTranslatedText.clicked.connect(self.execute)

    def execute(self) -> None:
        """
            Save translated text to DB
        """

        if not self.ui.translateBox.toPlainText():
            return None
        
        self.db.insertTranslate()   
