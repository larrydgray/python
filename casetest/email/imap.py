import imapclient
import pprint
import imaplib
imaplib._MAXLINE = 10000000
imapObj = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True)
imapObj.login('javacaverdude@yahoo.com','abplhoqkwzjrmype')
#pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs=imapObj.search(b'SINCE 20-Oct-2019')
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)
imapObj.logout()