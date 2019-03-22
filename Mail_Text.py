import smtplib
content = """"
 我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，smtplib 和email 库可以帮忙实现这个需求。smtplib 和 email 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等等。smtplib 是 Python 用来发送邮件的模块，email 是用来处理邮件消息。
发送普通文本的邮件，只需要 email.mime.text 中的 MIMEText 的 _subtype 设置为 plain。首先导入 smtplib 和 mimetext。创建 smtplib.smtp 实例，connect 邮件 smtp 服务器，login 后发送: 
"""
from email.mime.text import MIMEText
from email.header import Header


# 发送者
# sender = 'xx@xx.cn'
sender = 'xxx@189.cn'
# 接收者
receiver = 'xx@xx.cn'
# 邮件标题
# subject = 'python test send normal mail'
subject = '测试python发送普通邮件'
# 邮件服务器
# smtpserver = 'smtp.exmail.qq.com'
smtpserver = 'smtp.189.cn'
# 发邮件用户登录
# username= 'xx@xx.cn'
username = 'xxx@189.cn'
# 发邮件用户密码
# password = 'xxxxx'
password = 'xxxx'
# 发送邮件内容
msg = MIMEText(content,'plain','utf-8')
# 写如邮件标题
msg['Subject'] = Header(subject,'utf-8')
# 创建一个登录邮件服务器的类
smtp = smtplib.SMTP_SSL(smtpserver,465)
# 登录邮件服务器
try:
    smtp.connect(smtpserver)
    print('开始登录')
    # 输入登录邮件服务器用户名和密码
    smtp.login(username,password)
    print('登录成功')
    # 开始发送邮件了
    smtp.sendmail(sender,receiver,msg.as_string())
    print("邮件开始发送")
    #退出登录
    smtp.close()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("邮件发送失败",e)
