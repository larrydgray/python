import imapclient
import pprint
import imaplib
imaplib._MAXLINE = 10000000
# yahoo server is imap.mail.yahoo.com
# gmail is imap.gmail.com
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('javacaverdude@gmail.com',r'xxxxxx')
#pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs=imapObj.search('SUBJECT "LAC Moves"')
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)
imapObj.logout()