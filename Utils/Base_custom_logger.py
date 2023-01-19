"""Custom logger file"""
import inspect
import logging


class Base_custome_logger:
    def logging(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file handler object

        logger.setLevel(logging.DEBUG)
        return logger
