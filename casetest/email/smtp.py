import smtplib
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('javacaverdude@yahoo.com','xxxxxxxx')
smtpObj.sendmail('javacaverdude@yahoo.com',
                 'javacaverdude@gmail.com', 
                 'Subject: Test\n\n Testing email system.' )

smtpObj.quit()
