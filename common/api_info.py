import requests
import json
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from common.log_utils import logger

def get_access_token_apiget_access_token_api(session,HOSTS,secret,appid,grant_type='client_credential'):
    logger.info('开始验证是否能正常获取token_id')
    get_param_dict = {
        "grant_type":grant_type ,
        "appid":appid ,
        "secret": secret
    }
    try:
        response = session.get(url='https://%s/cgi-bin/token' %HOSTS,
                                    params=get_param_dict, verify=False)
        response = response.json()
    except RequestException as e:
        logger.error('调用获取access_token接口失败，原因是%s'%e.__str__())


    return response


def get_access_token_value(session,HOSTS):
    response = get_access_token_apiget_access_token_api(session,HOSTS,'65515b46dd758dfdb09420bb7db2c67f','wx55614004f367f8ca','client_credential')
    return response['access_token']

def create_user_tag_api(session,hosts,token_id,post_data):
    logger.info('调用create_user_tag接口')
    str_data = json.dumps(post_data, ensure_ascii=False)
    response = session.post(url='https://%s/cgi-bin/tags/create?access_token=%s' % (hosts,token_id),
                                 data=str_data.encode('utf-8')
                                 )
    return response