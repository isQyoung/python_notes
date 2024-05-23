import smtplib
import sys
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(toaddrs, msg):
    s = smtplib.SMTP(host="mail.xxx.com", port=587)
    s.starttls()
    username = 'alarm@xxx.com'
    passwd = '123456789'
    s.login(username, passwd)
    fromaddr = 'alarm@xxx.com'
    msg['From'] = fromaddr
    msg['To'] = ";".join(toaddrs)
    s.sendmail(from_addr=fromaddr, to_addrs=toaddrs, msg=msg.as_string())


if __name__ == '__main__':
    msg = MIMEMultipart()
    subject = Header(sys.argv[1], 'utf-8').encode()
    msg['Subject'] = subject
    text = MIMEText(str(sys.argv[2]), 'plain', 'utf-8')
    msg.attach(text)
    try:
        for i in sys.argv[3].split(','):
            print(i)
            fileApart = MIMEApplication(open(i, 'rb').read())
            fileApart.add_header('Content-Disposition', 'attachment', filename=i)
            msg.attach(fileApart)
    except:
        pass
    toaddrs = ['admin@xxx.com', 'user@xxx.com']
    # toaddrs = ['admin@cnwansun.com']
    send_mail(toaddrs=toaddrs, msg=msg)
    print("发送邮件成功")
