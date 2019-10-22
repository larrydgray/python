import os

for folderName, subfolders, filenames in os.walk('delicious2'):
    print('The current folder is '+ folderName)

    for subfolder in subfolders:
        print('SUBFOLDER Of '+folderName+': '+subfolder)
        for filename in filenames:
            print('FILE INSIDE '+folderName+': '+filename)
        print('')