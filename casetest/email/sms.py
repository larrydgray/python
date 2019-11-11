from twilio.rest import Client
accountSID = 'xxxxxx'
authToken = 'xxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12089532224'
aCellNumber = '+16093287422'
def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(to=aCellNumber, from_=myTwilioNumber, body=message)
textmyself('Testing 1.2.3. Testing, This has been a test of\
             your emergency sms broadcasting systeem. This\
            was only a test. Hi Thomas, sent from Python Script.') 