import time
print('Press ENTER to begin. Afterwards, \
    press ENTER to "click" the stopwatch. \
    Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time()- lastTime, 2)
        totalTime = round(time.time() - lastTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, 
            lapTime), end='')
        lapNum += 1
except KeyboardInterrupt:
    print('\nDone.')

