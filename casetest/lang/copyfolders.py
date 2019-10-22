import shutil, os, os.path
shutil.copytree('delicious','delicious2')
shutil.copytree('delicious2', 'delicious3')
shutil.rmtree('delicious')