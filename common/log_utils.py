import os
import logging
from logging import handlers

from common.config_utils import config
log_path = os.path.join(os.path.dirname(__file__),'../logs')


class LogUtils():
    def __init__(self,log_path = log_path):
        self.log_file_name = 'API_TEST_LOG'
        self.logger = logging.getLogger('API_TEST_LOG')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)

        file_handler = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),when='D',interval=1,backupCount=7,encoding='utf-8')
        # TimedRotatingFileHandler对象自定义日志级别
        file_handler.setLevel(logging.DEBUG)
        # TimedRotatingFileHandler对象自定义日志级别
        # rh.suffix = "%Y_%m_%d_%H_%M_%S.log"
        # TimedRotatingFileHandler对象自定义日志格式
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        console_handler.close()
        file_handler.close()

    def get_logger(self):
       return self.logger
logger = LogUtils().get_logger( )

if __name__ == '__main__':
    logger.warning('111')
