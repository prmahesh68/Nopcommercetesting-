import logging
class Logsetup:
    @staticmethod
    def getlog():
        logging.basicConfig(filename=".\\Logs\\testlog.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def getlogadd():
        logging.basicConfig(filename=".\\Logs\\custaddlog.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
