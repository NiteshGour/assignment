"""Custom logger file"""
import inspect
import logging
import configparser
import os

current_dir = os.getcwd()
config = configparser.RawConfigParser()
instance = 'Local'

if instance == 'Local':
    # for local machine
    PATH = "./polarisio_ui/Logs/logfile.log"


class LogGen:
    """Logger class"""

    @staticmethod
    def loggen():
        """Logger function"""
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler(PATH)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger
