import sys
import ui


class AppLifecycle():

    def __init__(self, app, db):
        self.app = app
        self.db = db

    def shutDown(self) -> None:
        """
            Correct exit from the program
        """

        self.app.close()
        self.db.close()
