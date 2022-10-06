import logging
from datetime import datetime
import os

class LogGenerator:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        dir = os.path.join(os.getcwd(),"Logs/"+datetime.now().strftime('%d_%m_%Y-%H_%M'))
        dir1 = os.mkdir(dir)
        fileHandler = logging.FileHandler(str(dir) +'/' +"automation_info.log")
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger