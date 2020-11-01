import requests
import unittest
from common.config_utils import config
from common.api_info import get_access_token_value


class TestCreatetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()


    def test_delete_tag(self):

        self._testMethodName = 'case04'
        self._testMethodDoc = '验证create_tag接口能否成功调用'
        # get_param_dict = {
        #     "grant_type": "client_credential",
        #     "appid": "wx55614004f367f8ca",
        #     "secret": "65515b46dd758dfdb09420bb7db2c67f"
        # }
        # response = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
        #                             params=get_param_dict, verify=False)
        # token_id = response.json()['access_token']
        token_id = get_access_token_value(self.session,self.HOSTS)
        post_data = {   "tag":{        "id" : 532   } }
        response =self.session.post( url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_data,verify = False)
        print(response.json())
        actual_result =response.json()['errmsg']
        self.assertEqual('ok',actual_result,'验证create_tag删除接口能否成功调用')

if __name__ == '__main__':
    unittest.main(verbosity=2)