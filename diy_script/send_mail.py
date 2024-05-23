#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_mail(toaddrs, msg):
    s = smtplib.SMTP(host="mail.xxx.com", port=25)
    s.starttls()
    username='admin@xxx.com'
    passwd='123456'
    s.login(username, passwd)
    fromaddr='admin@xxx.com'
    msg['From']=fromaddr
    msg['To']=toaddrs
    s.sendmail(fromaddr, toaddrs, msg.as_string())

if __name__ == '__main__':
    msg = MIMEMultipart()
    subject = Header('邮件主题a', 'utf-8').encode()
    msg['Subject'] = subject
    text = MIMEText('测试发送邮件b', 'plain', 'utf-8')
    msg.attach(text)
    toaddrs='user@xxx.com'
    send_mail(toaddrs, msg)
