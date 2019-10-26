import subprocess, webbrowser
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
subprocess.Popen(['c:\\Windows\\System32\\notepad.exe',
    'hello.txt'])
webbrowser.open('http://softwaredeveloperzone.com')
subprocess.Popen(['python','datetime_test.py'])