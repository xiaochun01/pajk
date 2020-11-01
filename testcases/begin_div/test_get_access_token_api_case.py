import requests
import unittest
from nb_log import LogManager

from common.config_utils import config
from common.api_info import get_access_token_apiget_access_token_api
from common import api_info
from common.log_utils import logger






class Test_GetaccesstokenApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
        self.logger = LogManager('ApiCase').get_logger_and_add_handlers()

    def tearDown(self) -> None:
        self.session.close()

    def test_get_accesstoken_success(self):
        requests.packages.urllib3.disable_warnings()
        self._testMethodName = 'case01'
        self._testMethodDoc = '验证get_access_token接口能否成功调用'
        logger.info('case01 验证get_access_token接口能否成功调用 --开始执行--11111')
        self.logger.info('case01 验证get_access_token接口能否成功调用 --开始执行--')
        # get_param_dict = {
        #     "grant_type": "client_credential",
        #     "appid": "wx55614004f367f8ca",
        #     "secret": "65515b46dd758dfdb09420bb7db2c67f"
        # }
        # response = self.session.get( url='https://%s/cgi-bin/token'%self.HOSTS,
        #                  params=get_param_dict,verify=False)
        response =  get_access_token_apiget_access_token_api(self.session,self.HOSTS,'65515b46dd758dfdb09420bb7db2c67f','wx55614004f367f8ca','client_credential')
        print(response)
        actual_result = response['expires_in']
        self.assertEqual(actual_result,7200,'case01 验证get_access_token接口能否成功调用')




    def test_get_accesstoken_error_appid(self):
        requests.packages.urllib3.disable_warnings()

        self._testMethodName = 'case02'
        self._testMethodDoc = '验证appid错误时，接口能否正常处理'
        # get_param_dict = {
        #     "grant_type": "client_credential",
        #     "appid": "wx55614004f367f8ca1",
        #     "secret": "65515b46dd758dfdb09420bb7db2c67f"
        # }
        # response = self.session.get( url='https://%s/cgi-bin/token'%self.HOSTS,
        #                  params=get_param_dict,verify=False)
        response =  get_access_token_apiget_access_token_api(self.session,self.HOSTS,'65515b46dd758dfdb09420bb7db2c67f','wx55614004f367f8ca1','client_credential')

        actual_result = response['errcode']
        self.assertEqual(actual_result,40013,'case02 验证appid错误接口能否成功调用')

    def test_get_accesstoken_error_secret(self):
        requests.packages.urllib3.disable_warnings()

        self._testMethodName = 'secret'
        self._testMethodDoc = '验证appidsecret错误时，接口能否正常处理'
        # get_param_dict = {
        #     "grant_type": "client_credential",
        #     "appid": "wx55614004f367f8ca",
        #     "secret": "65515b46dd758dfdb09420bb7db2c67f1"
        # }
        # response = self.session.get( url='https://%s/cgi-bin/token'%self.HOSTS,
        #                  params=get_param_dict,verify=False)
        response =  get_access_token_apiget_access_token_api(self.session,self.HOSTS,'65515b46dd758dfdb09420bb7db2c67f1','wx55614004f367f8ca','client_credential')

        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40001,'case03 验证secret错误接口能否成功调用')



if __name__=='__main__':
    unittest.main()