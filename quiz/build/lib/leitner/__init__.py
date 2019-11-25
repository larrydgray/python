from .leitner import *
import logging

logging.basicConfig(filename="leitner_log.txt",
    level=logging.DEBUG, 
    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Logging Leitner Module')
logging.info('Leitner modules are methods and classes that support the quiz.py app.')
logging.info('This is a efficient learning method. Google or Wiki Leitner Learning System.')
logging.info('This is where you are tested more often on things you get wrong and less often')
logging.info('on things you get right.')

