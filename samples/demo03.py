import logging
import os
from logging import handlers
import time

#创建一个logger日志对象
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)    #设置默认的日志级别

#创建日志格式对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#创建TimedRotatingFileHandler对象
rh = handlers.TimedRotatingFileHandler('test.log', when='S', interval=3, backupCount=5)
#TimedRotatingFileHandler对象自定义日志级别

rh.setLevel(logging.DEBUG)
#TimedRotatingFileHandler对象自定义日志级别
rh.suffix = "%Y_%m_%d_%H_%M_%S.log"
#TimedRotatingFileHandler对象自定义日志格式
rh.setFormatter(formatter)

logger.addHandler(rh)    #logger日志对象加载TimedRotatingFileHandler对象
#日志输出
logger.info('newdream')
time.sleep(3)


logger.info('newdream')
time.sleep(3)
logger.info('newdream')
time.sleep(3)
