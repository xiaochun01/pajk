import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('976110056@qq.com','kesabcsmsoflbfbe')

email_connet = 'from lllaa'





msg = MIMEText(email_connet,'html','utf-8')
msg['from'] = '976110056@qq.com'
msg['to'] ='2369483013@qq.com'
# msg['Cc'] ='976110056@qq.com'
msg['subject'] = '邮箱主题'
smtp.sendmail('976110056@qq.com','2369483013@qq.com',msg.as_string())

smtp.close()