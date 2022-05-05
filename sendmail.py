import smtplib
import ssl
import mysql.connector as m
import datetime as dt
import time
conn=m.connect(host="localhost",user="root",passwd="kshitij",database="newsletter")
c=conn.cursor()
senderemail="newsletterservice912@gmail.com"
password="agarwal123"
port=587
smtpserver="smtp.gmail.com"
context=ssl.create_default_context()
with smtplib.SMTP(smtpserver,port) as email:
    email.starttls(context=context)
    email.login(senderemail,password)
    c.execute("select * from news where time>=now() order by time")
    b=c.fetchall()
    for i in b:
        c.execute("select emailid from user where subscribed='{}'".format(i[0]))
        a=c.fetchall()
        sendtime=i[2]
        msg = f'Subject: {i[0]}\n\n{i[1]}'
        x=time.sleep(sendtime.timestamp()-time.time())
        for j in a:
            for k in j:
                email.sendmail(senderemail,k,msg)