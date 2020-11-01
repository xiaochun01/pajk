# import requests
# import unittest
# from common.config_utils import config
#
# session = requests.session()
# HOSTS = config.HOSTS
# session.close()
#
#
#
# requests.packages.urllib3.disable_warnings()
#
#
# get_param_dict = {
#     "grant_type": "client_credential",
#     "appid": "wx55614004f367f8ca",
#     "secret": "65515b46dd758dfdb09420bb7db2c67f"
# }
# response = session.get(url='https://%s/cgi-bin/token' % HOSTS,
#                             params=get_param_dict, verify=False)
# token_id = response.json()['access_token']
# print(token_id)
# post_data = {   "tag" : {     "name" : "广东浪子1111"  } }
# response =session.post( url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
#                              json=post_data,verify = False)
# print(response.json())
# actual_result =response.json()['tag']['name']
# print(actual_result)
# print(actual_result)
class Solution:
    def reverse(self,int):
        a = list(str(int))
        a.reverse()
        if int == 0:
            return 0
        while a[0]=='0':
            a.pop(0)
        if a[-1] == '-':
            a.insert(0,a.pop(-1))
        s = ''
        for i in a:
            s = s+i
        if eval(s) > pow(2,31)-1 or eval(s) < pow(-2,31):
            return 0
        return eval(s)
