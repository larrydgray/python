import threading
# incorrect way
# threadObj = threading.Tread(target=print('Cats','Dogs','Frogs',sep=' & '))
# print always returns None

threadObj = threading.Thread(target=print,
    args=['Cats','Dogs','Frogs'],kwargs={'sep': ' & '})
threadObj.start()
