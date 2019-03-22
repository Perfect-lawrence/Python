#!/usr/bin/env python
#-*- coding:utf8 -*-


import smtplib,sys
from email.mime.text import MIMEText
# 需求：发邮件给多个人

class Mstmp():
    def __init__(self,target,subject,content):
        #self.msg_from = 'pj_monitor@xxxx.com'
        self.msg_from = 'xxxx'
        #self.passwd = 'xxxx'
        self.passwd = 'xxxxx'
        #self.sender = smtplib.SMTP_SSL("smtp.mxhichina.com",465)
        self.sender = smtplib.SMTP_SSL("smtp.189.cn",465)
        self.msg_to = target.split(",")
        print(self.msg_to)
        self.subject = subject
        self.content = content

    def _login(self):
        self.sender.login(self.msg_from,self.passwd)

    def _msg(self):
        self.msg = MIMEText(self.content,"plain","utf-8") # 此处可选择文本格式或html等格式, 显示发送信息
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.msg_from
        self.msg['To'] = ",".join(self.msg_to)

    def send_mail(self):
        try:
            self._login()
            self._msg()
            # sendmail 第二个参数，目的邮箱，参数类型 str 或者 list
            self.sender.sendmail(self.msg_from,self.msg_to,self.msg.as_string())
        except smtplib.SMTPException as e:
            print("邮件发送失败，原因：{}".format( e))
        else:
            print("邮件发送至 {} 成功!".format(self.msg['To']))

        finally:
            self.sender.quit()


if __name__ == "__main__":
    rec = Mstmp(sys.argv[1],sys.argv[2],sys.argv[3])
    rec.send_mail()
