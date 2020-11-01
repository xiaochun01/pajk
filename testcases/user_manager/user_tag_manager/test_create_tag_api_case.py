import requests
import unittest
import json
from common.config_utils import config
from common.api_info import get_access_token_value
class TestCreatetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()


    def test_create_tag(self):
        requests.packages.urllib3.disable_warnings()

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
        # print(token_id)

        post_data = {   "tag" : {     "name" : "广东浪子"  } } #
        str_data = json.dumps(post_data,ensure_ascii=False)
        print(str_data)
        token_id = get_access_token_value(self.session,self.HOSTS)
        response =self.session.post( url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     data=str_data.encode('utf-8'),verify = False)#json传递数据时会把python字典中的中文转化为unicode编码
        print(response.json())
        actual_result =response.json()['tag']['name']
        self.assertEqual(actual_result,'广东浪子','验证create_tag接口能否成功调用')

if __name__ == '__main__':
    unittest.main(verbosity=2)