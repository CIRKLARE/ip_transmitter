from requests import get
import smtplib

ip = get("https://ifconfig.me").text

#print(ip)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #login to your testing gmail account
    server.login("your testing gmail", "password of testing email")
    #send ip to another gmail
    server.sendmail("your testing gmail", "your email" ,ip)
    server.close()
except:
    print("error")

