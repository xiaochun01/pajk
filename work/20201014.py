# # 1、利用requests模拟打开百度首页，并能通过正则随机取 左上角 新闻、hao123、地图、视频、贴吧、学术中的一个字符串进行输出
# # 2、利用requests中的session以及cookie的设置功能，完成 免登录进行回帖操作
# # 3、根据unitest讲解的线性接口测试框架基础部分，构建类似的接口测试项目
# # 4、整理课堂所学内容
# #-------------------------------------------------------------------
# from collections import OrderedDict
#
# import requests
# import re
# import random
#
# ses = requests.session()
# # hosts = 'www.baidu.com'
# #
# # response = ses.get(url='https://www.baidu.com/')
# # body = response.content.decode('utf-8')
# #
# # response_title = re.findall('class=mnav>(.+?)</a> ',body)
# # n =random.randint(0,len(response_title)-1)
# # print(response_title[n])
#
#
# #-------------------------------------------------------------------
# # hosts = '47.107.178.45'
# #
# # response = ses.get(url='http://%s/phpwind/'%hosts)
# # body = response.content.decode('utf-8')
# # token_id = re.findall('name="csrf_token" value="(.+?)"',body)[0]
# # # ses.cookies.set('zFb_lastvisit','2014%091602601207%09%2Fphpwind%2Findex.php%3Fm%3Du%26a%3Dshowcredit',path='/',domain='47.107.178.45')
# # # ses.cookies.set('zFb_winduser','aRxM%2BgUYj8KdR3Xu6IufVybDDvRY748yfHmjEJOWMihSLc%2BnETVQZmciFMA%3D',path='/',domain='47.107.178.45')
# #
# # form_data = OrderedDict(
# #     [
# #         ("atc_title",(None,'回购价格33都111')),
# #        ("atc_content",(None,'都i化工33i放倒钩111i都')),
# #         ("pid",(None,'')),
# #         ("tid",(None,'89485')),
# #         ("special",(None,'')),
# #         ("reply_notice",(None,'1')),
# #         ("csrf_token", (None, token_id))
# #     ]
# # )
# # response = ses.post(url='http://%s/phpwind/index.php?c=post&a=doreply&_json=1&fid=81'%hosts,
# #                     files=form_data)
# #
# # print(response.text)
# #
#
#
#
# --------------------------------------
# 添加cookie
#
# #方式一
# # session.cookies['company_name']='newdream'
# # response = session.get(url='http://www.hnxmxit.com/')
#
# # 方式二(推荐)
# session.cookies.set('company_name','newdream',path='/',domain='47.107.178.45')
# response = session.get(url='http://www.hnxmxit.com/')
#
# #方式三
# # cookie_dict = {"company_name":"newdream"}
# # requests.utils.add_dict_to_cookiejar(session.cookies,cookie_dict)
# # response = session.get(url='http://www.hnxmxit.com/')
#
# # #方式四
# # cookie_object = requests.cookies.RequestsCookieJar()
# # cookie_object.set('company_name','newdream')
# # session.cookies.update(cookie_object)
# # response = session.get(url='http://www.hnxmxit.com/')
#
#
#
# ------------------------------------------------------------------------
# re模块的使用
# 通过实例化对象
# pattern = re.compile('12\D45')  #\d 0--9
# result1 = re.match(pattern,str1)    # match()匹配以指定的模版开头的字符串
#
# print( result1.group() )
#
# #方式二：
# 直接使用
# result2 = re.match('12\D45',str1)
# print( result2.group() )
#
# #方法三：
# str3 = 'NeWdream'
# result3 = re.match('new',str3,flags=re.IGNORECASE)
# print( result3.group() )
#
# -----------------------------------
# 'w'：字母、数字、下划线  '+'表示多个
# re.search() 全部匹配，返回的是对象需要在   re.search('n\w+a','匹配字符').group() 才能输出
# re.match() 开头匹配，返回的是对象需要在   re.search().group() 才能输出
# re.split()匹配字符模版 根据匹配到的字符模版把string进行切割，返回一个列表
# re.findall()以string列表形式返回string中pattern的所有非重叠匹配项
# re.finditer() 匹配整个string 返回一个顺序访问每个匹配结果的迭代器,只能用来遍历操作
# re.sub()替换
# str6 = "newdream common !"
# #group含义
# value6 = re.search("(\w+) (\w+)",str6)
# print( value6.group(2) )  # 默认值0  默认组 0 表示匹配的内容 ()新组 1 0 1  2
# value8 = re.sub("(\w+) (\w+)",r"\2 hello",str6)  # r 表示原生字符串
# print( value8 )
# re.subn()#subn 替换，比sub增加了指定替换次数 返回的是一个元祖
#
# ---------------随机数应用
# import random
# n = random.randint('开始数字','结束数字')
#
# -------------------------断言
# assertEqual('a','b','如果a和b不相等就输出')
# assertTure('','如果布尔类型不为真等就输出')
# self.assertIn('a','b','如果a不在b中就输出')
#
#
# ----------------------用例执行
# 在用例函数前加
# @unittest.skip('就是不想执行')  # 无条件跳过
# @unittest.skipIf(True, '条件为真时跳过')
# @unittest.skipUnless(False, '条件为假跳过')
# @unittest.expectedFailure  # 不统计用例执行的失败结果
#
# ----------------添加用例执行集合
# # 方式一：
# # test_suite = unittest.TestSuite()
# # test_suite.addTest(TestDemo12_01('test_add_01')) # 模块下的类1
# # test_suite.addTest(TestDemo12_02('test_add_005')) # 模块下的类2
# # test_suite.addTest(TestDemo10_2('test_add_01')) # 其它模块下的类
# # unittest.main(defaultTest='test_suite')
#
# # 方式二：
# test_suite = unittest.TestSuite(unittest.makeSuite(TestDemo12_02))
# unittest.main(defaultTest='test_suite')
#
# # 方式三：
# # test_suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo13_02) #类下的所有用例
# # test_suite = unittest.TestLoader().loadTestsFromModule(test_demo_12) #模块下的所有用例
# # loadTestsFromName() 通过字符串的方式引入用例 单个用例 单个类 单个模块
# # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01.test_add_01')
# test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01')
# # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12')
#
# # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_13.TestDemo13_02.test_add_01')
# unittest.main(defaultTest='test_suite')
#
# # 方式四：
# test_suite_01 = unittest.TestSuite(unittest.makeSuite(TestDemo10))
# test_suite_02 = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01')
#
# all_suite = unittest.TestSuite()
# all_suite.addTests(test_suite_01)
# all_suite.addTests(test_suite_02)
#
# unittest.main(defaultTest='all_suite')
#
#
#
# ------------------------匹配用例集合
#
# import unittest
# import os
#
# case_path = os.path.join(os.path.dirname(__file__),'test_suite')
#
# discover = unittest.defaultTestLoader.discover(start_dir=case_path,
#                                                pattern='test_demo*.py',
#                                                top_level_dir=case_path)
# all_suite = unittest.TestSuite()
# all_suite.addTest( discover )
#
# unittest.main(defaultTest='all_suite')
#
#
# ------------测试报告
# # # 初级报告 verbosity=2
# # unittest.main(defaultTest='all_suite',verbosity=2)
# #
# # # TextTestRunner 报告 可以把报告保存到文件里面
# #
# # # stream=None 表示测试结果在控制台显示
# # text_runner = unittest.TextTestRunner(stream=None,verbosity=2,descriptions=None)
# # text_runner.run( all_suite )
# #
# # # 文本格式报告
# # report_file_path = os.path.join(os.path.dirname(__file__),'report','report.txt')
# # with open(report_file_path,'w',encoding='utf-8') as file:
# #     text_runner = unittest.TextTestRunner(stream=file, verbosity=2, descriptions='newdream')
# #     text_runner.run(all_suite)
#
# # HTML格式报告
# html_file_path = os.path.join(os.path.dirname(__file__),'report','report01.html')
# html_file = open(html_file_path,'w+')
# html_runner = HTMLTestRunner.HTMLTestRunner(stream=html_file,
#                                             title='newdreamP3P4',
#                                             description="测试实战")
# html_runner.run(all_suite)
#
# ----------------------测试执行结果调试
#
#
# import unittest
# import os
# import HTMLTestReportCN
#
# case_path = os.path.join(os.path.dirname(__file__),'test_suite')
#
# discover = unittest.defaultTestLoader.discover(start_dir=case_path,
#                                                pattern='test_demo*.py',
#                                                top_level_dir=case_path)
# all_suite = unittest.TestSuite()
# all_suite.addTest( discover )
#
# report_path = os.path.join(os.path.dirname(__file__),'report/')
# report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
# report_dir.create_dir('API_TEST') #调用创建目录的方法
# report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
# report_html_file = open( report_html_path,'wb' )
# html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
#                                               title='接口测试报告',
#                                               description='实战使用',
#                                               tester='P3P4')
# html_runner.run(all_suite)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#----------------------------博客园回帖
import requests

# 博客园回复操作
requests.packages.urllib3.disable_warnings()

session = requests.session()

header_info = {
    "accept":"application/json, text/javascript, */*; q=0.01",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "content-type":"application/json; charset=UTF-8"
}

post_data = {
	"postId": 13737302,
	"body": "再次支持你",
	"parentCommentId": 0
}

session.cookies.set('__gads','ID=6412e60d0a3a58ef:T=1589693568:S=ALNI_MaK6JuQJ-00Ep9wmxY1kL7eeBdThw',path='/',domain='.cnblogs.com')
session.cookies.set('_ga','GA1.2.1747552024.1589693682',path='/',domain='.cnblogs.com')
session.cookies.set('UM_distinctid','17420f5a9e9607-0b41310ed78756-3323765-1fa400-17420f5a9ebd80',path='/',domain='.cnblogs.com')
session.cookies.set('Hm_lvt_39b794a97f47c65b6b2e4e1741dcba38','1601134611,1601134614,1601134626,1601166984',path='/',domain='.cnblogs.com')
session.cookies.set('.Cnblogs.AspNetCore.Cookies','CfDJ8AHUmC2ZwXVKl7whpe9_lauGiccjCPnciHh42OWSaqLtkE9ulTCZX79TSUk5SsPr4WbS-4MpbTxat5GbG4g_tcQdM9mMHY0SVG10PrP30KsPMN04-MFSA3ZkyECDMwr2NkwHZgHDVYhg7BU75AkVD7O38eVc4NHU67Ym-RqFks0Rq_3cjQ5EfkhrdTe3RBJQzGRdZIJ5etoU4emmhSq58kVB_OHFAqF-LqYoACpUrRnFbWE3_y9ki_zBQLKvJUkF3cTjTSXUm9LVoEZBc9t4NT1NqqrdN0jEoC8zRILN9j21WLvTLJWSEHGAydz5clvGakNFHL1D-p4i19jSliU7SCgKrDMI_3FEFua1w1NG56u_6lspHW8jNVzjs7DmXnXNrTNOLYeZPIqhkzrp5_aaSRgpWOKLNaJA1apt-t5_4HzmoWBKRhw6tLYQEUs6Y1uZ2FZ1NYiux7t9lRliPAIhkfRvDkb-W1p92ZuKHCFoRopnixOmeTQ3l7x-m6LdJxL0cTXsqk1ccgO1vENs3f591bHMEHoI3h49vn9f4QoqjUMqn_luD2BRHIpbA83ftWJhL0CyeS3fo4fgK-tjdiWlNjg',path='/',domain='.cnblogs.com')
session.cookies.set('_gid','GA1.2.1045122852.1602945794',path='/',domain='.cnblogs.com')
session.cookies.set('_gat','1',path='/',domain='.cnblogs.com')

response = session.post(url='https://www.cnblogs.com/xiaochunrihe/ajax/PostComment/Add.aspx',
                        json=post_data,verify = False)