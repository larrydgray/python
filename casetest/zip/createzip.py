import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
#newZip = zipfile.ZipFile('new.zip', 'a')  adds to a zip file
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()