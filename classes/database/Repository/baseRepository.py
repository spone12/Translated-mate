from classes.logger import Logger

class BaseRepository:
    def __init__(self):
        #self.logger = Logger().getLogger(self.__class__.__name__)
        self.logger = Logger()
