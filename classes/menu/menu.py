import sys
import ui

class Menu():

    def __init__(self, program, db):
        self.program = program
        self.db = db

    def exitProgramm(self) -> None:
        """
            Correct exit from program
        """

        self.program.close()
        self.db.close()
