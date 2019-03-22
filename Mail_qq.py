#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr



# 发件人
sender='xx@xx.cn'
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
login_password = 'xx'
stmp_server = "smtp.exmail.qq.com"
# 收件人邮箱账号
receiver = 'xx@xxx.com'

content = """"
 我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，smtplib 和email 库可以帮忙实现这个需求。smtplib 和 email 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等等。我们这里将会分几节把发送邮件功能解释完成。
smtplib 是 Python 用来发送邮件的模块，email 是用来处理邮件消息。
发送普通文本的邮件，只需要 email.mime.text 中的 MIMEText 的 _subtype 设置为 plain。首先导入 smtplib 和 mimetext。创建 smtplib.smtp 实例，connect 邮件 smtp 服务器，login 后发送: 
"""

def mail():
    result = True
    try:
        # 邮件内容
        msg = MIMEText(content,'plain','utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(['xxx',sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(['别名',receiver])
        # 邮件的主题 
        msg['Subject'] = "使用腾讯企业邮箱发送邮件测试"
        # 登录邮件服务器
        mail_server = smtplib.SMTP_SSL(stmp_server,465)
        # 登录邮件服务器用户名和登录密码
        mail_server.login(sender,login_password)
        # 开始发送邮件
        mail_server.sendmail(sender,receiver,msg.as_string())
        # 发送完成断开连接
        mail_server.close()
    except smtplib.SMTPException as e:
        result = False
    return result
result = mail()

if result:
    print("邮件发送成功")
else:
    print("邮件发送失败")
