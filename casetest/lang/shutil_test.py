import shutil, os, os.path
os.chdir('C:\\dev\\github\\python\\casetest\\lang')
if not os.path.exists('delicious'):
    os.mkdir('delicious')
    os.mkdir('delicious\dir1')
    os.mkdir('delicious\dir2')
shutil.copy('spam.txt', 'delicious.txt')
shutil.copy('eggs.txt', "delicious\\eggs2.txt")
shutil.copy('delicious\\eggs2.txt','delicious\\dir1\\eggs3.txt')
shutil.copy('delicious\\eggs2.txt','delicious\\dir2\\eggs4.txt')
