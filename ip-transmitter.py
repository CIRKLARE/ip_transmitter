from requests import get
import smtplib

ip = get("https://ifconfig.me").text

#print(ip)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login("your testing gmail", "password")
    server.sendmail("your testing gmail", "your email" ,ip)
    server.close()
except:
    print("error")

