import sys
import ui

class Menu():

    def __init__(self, program):
        self.program = program

    def exitProgramm(self) -> None:
        """
            Correct exit from program
        """

        self.program.close()
        