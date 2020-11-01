import logging




logger = logging.getLogger('')

logger.setLevel(logging.DEBUG) #设置日志默认
formatter = logging.Formatter("%(asctime)s--%(name)s %(levelname)s- %(message)s")

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)

fh = logging.FileHandler('../logs/test.log', 'a', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)






logger.addHandler(sh)
logger.addHandler(fh)

logger.debug('222')