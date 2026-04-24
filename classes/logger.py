import logging
import os
from pprint import pprint

class Logger():
    """
        Logger class
    """

    def __init__(self):
        self.logPath = "log/"

    def log(self, logClass: str, message: str, level = 'error') -> None:

        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        logging.basicConfig(
            level    = logging.INFO,
            filename = self.logPath + logClass + "_errors.log",
            filemode = "a",
            format   = "%(asctime)s [%(levelname)s]: %(message)s"
        )
        logging.error(message) 
        print(message)

    def printObject(obj) -> None:
        pprint(vars(obj))
        