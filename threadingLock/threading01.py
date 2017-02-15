import threading

def do_this():

    global dead
    x = 0

    print "This is our thread!"
    while not dead:
        x += 1
        pass
    print x

def main():

    global dead
    dead = False

    our_thread = threading.Thread(target=do_this, name = "Ourthread")
    our_thread.start()

    print threading.active_count()
    print threading.enumerate()
    print our_thread.is_alive()

    raw_input("Hit enter to die.")
    dead = True

    raw_input("The thread has died. wait a bit, and hit enter again")

    print our_thread.is_alive()
if ( __name__ == "__main__"):
    main()

