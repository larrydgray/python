#!/usr/bin/python

import smtplib
import base64

filename = "test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'javacaverdude@yahoo.com'
receiver = 'javacaverdude@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement for game turn data.
"""
# Define the main headers.
part1 = """From:<%s>
To:<%s>
Subject: Sending Attachement Game Moves
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" %(sender, receiver, marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" %(body,marker)



# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3
print('------------ email --------------')
print(part1)
print('-----------------------------------')
print(part2)
print('----------------------------------')
print(part3)
print('-------------Messsage-------------')
print(message)

try:
    smtpObj = smtplib.SMTP('smtp.mail.yahoo.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('javacaverdude@yahoo.com','xxxxxx')
    smtpObj.sendmail(sender, receiver, message)
    smtpObj.quit()
    print ("Successfully sent email")
except Exception as e:
    print ("Error: unable to send email")
    print (e)