import smtplib
from email.mime.text import MIMEText
from email.header import Header
from basic_mail_op.op_storage import temp_storage
import random
pass1='qimddlwbnympbfai'
pass2='pehiokuarlmibdcd'
class Email:
    def __init__(self,password=pass1):
        self.password=password
        self.smtp = smtplib.SMTP()
        self.connect()
    def connect(self):
        self.smtp.connect('smtp.qq.com',25)
        print('连接成功')
        self.smtp.login('798637048@qq.com', pass2)
        print('登陆成功')

    def close(self):
        self.smtp.quit()

    def send_email(self,name,email_address):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        v_code=random.randint(1000,9999)
        message = MIMEText('Note Your Life的验证码为:'+str(v_code), 'plain', 'utf-8')
        message['From'] = Header("Note Your Life的开发团队", 'utf-8')  # 发送者
        message['To'] = Header("尊敬的玩家", 'utf-8')  # 接收者
        subject = 'Note Your Life的验证码'
        message['Subject'] = Header(subject, 'utf-8')
        self.smtp.sendmail('798637048@qq.com', email_address, message.as_string())
        temp_storage[name]=v_code
        print('发送成功')

email=Email()