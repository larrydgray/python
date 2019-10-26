import subprocess
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['start', 'hello.txt'],shell=True)