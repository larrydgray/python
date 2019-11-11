import imaplib
import pprint
import email
imaplib._MAXLINE = 10000000
def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select('INBOX', readonly=True)
    #m.select()
    return m
def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, None, '(BODY.PEEK[])')
    email_body = data[0][1]
    mail = email.message_from_string(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))
# yahoo server is imap.mail.yahoo.com
# gmail is imap.gmail.com
#imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login('javacaverdude@gmail.com',r'Je;AcY{m}S@=')
#pprint.pprint(imapObj.list_folders())
#imapObj.select_folder('INBOX', readonly=True)
imapObj = connect('imap.gmail.com','javacaverdude@gmail.com',r'xxxxx')

UIDs=imapObj.search('SUBJECT "LAC Moves"')
for UID in UIDs:
    downloaAttachmentsInEmail(imapObj, UID, './download/')