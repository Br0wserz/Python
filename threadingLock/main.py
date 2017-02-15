#!/usr/bin/python

__author__ = 'User'

import threading
import time
import random

class counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  #Definisco self.lock come un lucchetto

    def increaseCounter(self):
        self.lock.acquire()  #Serve per bloccare l'accesso al lock
        self.count += 1
        self.lock.release()  #Serve per aprire l'accesso al lock

    def __str__(self):
        return str(self.count)


## MAIN ##

def thread_function(c):
    print threading.currentThread().getName(), ' starting'
    pause = random.random()
    print threading.current_thread().getName(), ' waiting for %.2f seconds' % pause
    time.sleep(pause)
    c.increaseCounter()
    print threading.currentThread().getName(), ' contatore = ', c
    print threading.currentThread().getName(), ' ending'

c = counter()

for i in range(4):
    t = threading.Thread(target = thread_function, args = (c,))
    t.start()


