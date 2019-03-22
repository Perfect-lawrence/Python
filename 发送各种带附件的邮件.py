#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 需求：发送各种带附件的邮件

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

def Mail():
    # 发件人
    sender = "xx@xx.cn"
    # 邮件标题
    subject = "Python测试发送多人邮件并带各种附件"
    # 邮件服务器
    smtp_server = 'smtp.exmail.qq.com'
    #登录邮件用户名和密码
    username = "xx@xx.cn"
    password = "xx"
    # 收件人邮箱账号列表
    receivers = ['xxx@xx.cn','xx@xx.com','xx@189.cn']

    content = """"
     我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，smtplib 和email 库可以帮忙实现这个需求。smtplib 和 email 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等。smtplib 是 Python 用来发送邮件的模块，email 是用来处理邮件消息。 发送普通文本的邮件，只需要 email.mime.text 中的 MIMEText 的 _subtype 设置为 plain。首先导入 smtplib 和 mimetext。创建 smtplib.smtp 实例，connect 邮件 smtp 服务器，login 后发送使用MIMEMultipart来标示这个邮件是多个部分组成的，然后attach各个部分。如果是附件，则add_header加入附件的声明。MIME有很多种类型，这个略麻烦，如果附件是图片格式，我要用MIMEImage，如果是音频，要用MIMEAudio，如果是word、excel，我都不知道该用哪种MIME类型了
    """
    # 发送文本内容
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    # 发送带  图片 附件内容
    imageFile = 'kubernetes.png'
    imageApart = MIMEImage(open(imageFile,'rb').read(),imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment',filename=imageFile)

    # 发送带  PDF 附件的内容
    pdfFile = 'postgresql-11-A4.pdf'
    pdfApart= MIMEApplication(open(pdfFile,'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)

    # 发送带  压缩包 附件的内容
    zipFile = 'resume_template.zip'
    zipApart = MIMEApplication(open(zipFile,'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment',filename=zipFile)

    # 发送带 Excel或 Word 附件的内容
    wordFile = 'safe.doc'
    wordApart = MIMEApplication(open(wordFile,'rb').read())
    wordApart.add_header('Content-Disposition', 'attachment',filename=wordFile)

    f = MIMEMultipart()
    f.attach(msg)
    f.attach(imageApart)
    f.attach(pdfApart)
    f.attach(zipApart)
    f.attach(wordApart)
    f['Subject'] = subject
    try:
        result = True
        mail_server = smtplib.SMTP_SSL(smtp_server, 465)
        mail_server.login(username, password)
        mail_server.sendmail(msg['From'], msg['To'].split(','), f.as_string())
        mail_server.close()
    except smtplib.SMTPException as e:
        result = False
    return result

if __name__ == '__main__':
    successful = Mail()
    if successful:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
