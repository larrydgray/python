from twilio.rest import Client
accountSID = 'xxxxxx'
authToken = 'xxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+155555555555'
myCellNumber =   '+155555555555'
message = twilioCli.messages.create(to=myCellNumber, 
   from_=myTwilioNumber, body='Mr. Watson - Come Here\
  - I want to see you.')
print(message.to)
print(message.from_)
print(message.body)
print(message.status)
print(message.date_created)
print(message.date_sent)
print(message.sid) 
updatedMessage = twilioCli.messages.get(message.sid)
#print(updatedMessage.status)
#print(updatedMessage.date_sent)
def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(to=myCellNumber, from_=myTwilioNumber, body=message)
textmyself('Testing 1.2.3. Testing, This has been a test of\
             your emergency sms broadcasting systeem. This\
            was only a test')  