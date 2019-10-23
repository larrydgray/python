import zipfile, os, pprint
os.chdir('C:\\dev\github\python\casetest\zip')
exampleZip = zipfile.ZipFile('stuff.zip')
pprint.pprint(exampleZip.namelist())

