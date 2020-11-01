import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('976110056@qq.com','kesabcsmsoflbfbe')  #邮箱授权码

msg = MIMEMultipart()

msg['from']='976110056@qq.com'
msg['to'] = '2369483013@qq.com'
msg['Cc'] = '2369483013@qq.com'
msg['subject'] = '测试邮件'

email_connet = 'from test..'
msg.attach(MIMEText(email_connet,'html','utf-8'))

attach_file_path = os.path.join(os.path.dirname(__file__),'API_TEST_V2.5.html')
attach_file_job = MIMEText(open(attach_file_path,'rb').read(),'base64','utf-8')
attach_file_job['Content-Type'] = 'application/octet-stream'
attach_file_job.add_header('Content-Disposition','atachment',
                           filename=('gbk','',os.path.basename(attach_file_path)))
msg.attach( attach_file_job )
smtp.sendmail('976110056@qq.com',['2369483013@qq.com','2369483013@qq.com'],msg.as_string()) #发件人、收件人

smtp.close()