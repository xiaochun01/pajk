import os
import configparser

# coding=utf-8


config_file_path = os.path.join(os.path.dirname(__file__),'..','config','localconfig.ini')

class ConfigUtils():
    def __init__(self,config_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_file_path,encoding='utf-8')
    @property #类中的一个方法 ，属性方法
    def HOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    @property
    def RERORT_PATH(self):
        report_path_value = self.cfg.get('default','RERORT_PATH')
        return report_path_value
    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('default','LOG_PATH')
        return log_path_value
    @property
    def LOG_LEVEL(self):
        log_level_value = self.cfg.get('default','LOG_LEVEL')
        return log_level_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('default', 'SMTP_RECEIVER')
        return smtp_receiver_value


config =ConfigUtils()
if __name__ == '__main__':
    print(config.LOG_PATH)

