import zipfile, os
os.chdir('C:\\dev\github\python\casetest\zip')
stuffZip = zipfile.ZipFile('stuff.zip')
stuffZip.extractall()
stuffZip.close()
