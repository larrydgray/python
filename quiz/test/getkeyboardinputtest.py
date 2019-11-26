import msvcrt, sys
while True:
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        #if ch in '\x00\xe0':  # arrow or function key prefix?
        #    ch = msvcrt.getch()  # second call returns the scan code
        if ch == b'q':
            print ("Q was pressed")
        elif ch == b'\r':
            print('Enter wa pressed')
        elif ch == b'x':
            sys.exit()
        else:
            print ("Key Pressed:", ch)