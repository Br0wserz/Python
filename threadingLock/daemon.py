import threading
import logging
import time


def daemon():
    logging.debug('starting...')
    time.sleep(2)
    logging.debug('exiting...')

def non_daemon():
    logging.debug('starting...')
    logging.debug('exiting...')

logging.basicConfig(level = logging.DEBUG, format = '%(threadName)s %(message)s')

d = threading.Thread(target = daemon, name = 'daemon')
d.setDaemon(True) #that runs without blocking the main program from exiting
t = threading.Thread(target= non_daemon, name = 'non_daemon')

d.start()
t.start()

d.join(1)
print d.isAlive()
t.join(0)

