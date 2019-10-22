import traceback
def doSomething(size):
    if size<5:
        raise Exception('Size of '+str(size)+' is less than 5!')
    if size>10:
        raise Exception('Size of '+str(size)+' is more than 10!')
    print('Size of '+str(size)+' is just right.')
def tryDoSomething(size):
    try:
        doSomething(size)
    except:
        errorFile = open('errors.txt','a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info wass written to errorInfo.txt')
tryDoSomething(1)
tryDoSomething(22)
tryDoSomething(6)
tryDoSomething(8)