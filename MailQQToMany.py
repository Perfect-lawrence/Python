#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 需求 发送邮件给多个人

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def Mail():
    sender = "xx@xx.cn"
    receivers = ['xx@xx.cn','xx@xx.com','xx@189.cn']

    subject = "Python测试发送多人邮件"
    smtp_server = 'smtp.exmail.qq.com'

    username = "xx@xx.cn"
    password = "xxx"

    content = """"
    我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，smtplib 和email 库可以帮忙实现这个需求。smtplib 和 email 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等等。
    smtplib 是 Python 用来发送邮件的模块，email 是用来处理邮件消息。发送普通文本的邮件，只需要 email.mime.text 中的 MIMEText 的 _subtype 设置为 plain。首先导入 smtplib 和 mimetext。创建 smtplib.smtp 实例，connect 邮件 smtp 服务器，login 后发送: 
"""
    result = True
    try:
        msg = MIMEText(content,'plain','utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receivers)

        mail_server = smtplib.SMTP_SSL(smtp_server,465)
        mail_server.login(username,password)
        mail_server.sendmail(msg['From'],msg['To'].split(','),msg.as_string())

    except smtplib.SMTPException as e:
        result = False
    return result
successful = Mail()
if successful:
    print("邮件发送成功")
else:
    print("邮件发送失败")
