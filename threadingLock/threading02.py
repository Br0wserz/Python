import threading

def do_this():

    global x, lock

    lock.acquire()
    try:
        while x < 300:
            x += 1

        print x
    finally:
        lock.release()

def do_after():

    global x, lock
    lock.acquire()
    try:
        x = 450
        while x < 600:
            x += 1

        print x
    finally:
        lock.release()

def main():

    global x, lock

    x = 0

    lock = threading.Lock()


    our_thread = threading.Thread(target=do_this)
    our_thread.start()

    our_next_thread = threading.Thread(target=do_after)
    our_next_thread.start()

if ( __name__ == "__main__"):
    main()

