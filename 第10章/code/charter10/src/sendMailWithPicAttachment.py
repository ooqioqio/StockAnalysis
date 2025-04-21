# !/usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 发送邮件
def sendMail(username,pwd,from_addr,to_addr,msg):
    try:
        smtp = smtplib.SMTP() 
        smtp.connect('smtp.163.com') 
        smtp.login(username, pwd) 
        smtp.sendmail(from_addr,to_addr, msg) 
        smtp.quit()
    except Exception as e:  
        print(str(e))
HTMLContent = '<html><head></head><body>'\
 '<h1>Hello</h1>This is <a href="https://www.cnblogs.com/JavaArchitect/">My Blog.</a>'\
 '<img src="cid:picAttachment"/>'\
 '</body></html>'        
message = MIMEMultipart()
body = MIMEText(HTMLContent, 'html', 'utf-8')
message.attach(body)
message['Subject'] = 'Hello,用Python发送邮件'
message['From'] = 'hsm_computer@163.com'                # 邮件上显示的发件人
message['To'] ='hsm_computer@163.com,153086207@qq.com'  # 故意显示两个收件人
imageFile = MIMEImage(open('D:\\stockData\\ch10\\picAttachement.jpg', 'rb').read())
imageFile.add_header('Content-ID', 'picAttachment')
imageFile['Content-Disposition'] = 'attachment;filename="picAttachement.jpg"'
message.attach(imageFile)
sendMail('hsm_computer','xxx','hsm_computer@163.com','hsm_computer@163.com',message.as_string())