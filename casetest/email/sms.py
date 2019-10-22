from twilio.rest import Client
accountSID = 'AC04e57b8c86c1241d57f864d53b8983cf'
authToken = '3954e685973587ac2e93bc73de61ae04'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12089532224'
aCellNumber = '+16093287422'
def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(to=aCellNumber, from_=myTwilioNumber, body=message)
textmyself('Testing 1.2.3. Testing, This has been a test of\
             your emergency sms broadcasting systeem. This\
            was only a test. Hi Thomas, sent from Python Script.') 