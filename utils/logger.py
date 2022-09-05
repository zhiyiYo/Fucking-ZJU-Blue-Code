# coding:utf-8
import logging
from pathlib import Path


class Logger:

    log_dir = Path('log')

    def __init__(self, fileName: str):
        """
        Parameters
        ----------
        fileName: str
            log filename which doesn't contain `.log` suffix
        """
        self.log_dir.mkdir(exist_ok=True, parents=True)

        self._logger = logging.getLogger(fileName)
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(
            self.log_dir/(fileName+'.log'), encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(fmt)

        self._logger.addHandler(file_handler)

    def info(self, msg):
        logging.getLogger("uvicorn.info").info(msg)
        self._logger.info(msg)

    def error(self, msg, exc_info=False):
        logging.getLogger("uvicorn.error").error(msg)
        self._logger.error(msg, exc_info=exc_info)

    def debug(self, msg):
        logging.getLogger("uvicorn.debug").debug(msg)
        self._logger.debug(msg)

    def warning(self, msg):
        logging.getLogger("uvicorn.warning").warning(msg)
        self._logger.warning(msg)

    def critical(self, msg):
        logging.getLogger("uvicorn.critical").critical(msg)
        self._logger.critical(msg)


logger = Logger("app")
