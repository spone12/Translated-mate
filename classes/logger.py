import logging
import os


class Logger:
    _instance = None

    def __new__(cls, logDir: str = "log"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(logDir)
        return cls._instance

    def _init(self, logDir: str):
        self.logDir = logDir
        os.makedirs(self.logDir, exist_ok=True)
        self.loggers = {}

    def getLogger(self, name: str):
        """ Get logger """
        if name in self.loggers:
            return self.loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler(
            os.path.join(self.logDir, f"{name}.log")
        )
        consoleHandler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(consoleHandler)
            logger.addHandler(fileHandler)

        self.loggers[name] = logger
        return logger
