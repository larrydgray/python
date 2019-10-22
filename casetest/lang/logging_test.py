
import logging
#logging.disable(logging.DEBUG)
logging.basicConfig(filename="log.txt",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Logging Program')
logging.info('This is a app that test python loggging.')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'%(n))
    total=1
    for i in range(n+1):
        total *= i 
        logging.debug('i is '+str(i)+', total is '+str(total))
    logging.debug('End of facctorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.warning('This is a warning.')
logging.error('This is an error!')
logging.critical('This is a critical problem!!!!!!!')
logging.debug('End of Program')
logging.disable()
logging.debug('More loggging')
