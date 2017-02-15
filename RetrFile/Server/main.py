import imp
from threading import Thread
import os
MySocket = imp.load_source('FullSocket', r"C:\Users\Stefano\PycharmProjects\RetrFile\libs\FullSocket")

BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)

    def run(self):
        new_path = 'files/'
        while True:
            try:
                filename = self.sock.recv()
                path = "C:/Users/Stefano/PycharmProjects/RetrFile/"+new_path
                dirs = os.listdir(path)
                if os.path.isfile(path+filename):
                    self.sock.send('EXISTS ' + str(os.path.getsize(path+filename)))
                    userResponse = self.sock.recv()
                    if userResponse[:2] == 'OK':
                        with open(path+filename, 'rb') as f:
                            while True:
                                bytesToSend = f.read(BUFFER_SIZE)
                                if bytesToSend == '':
                                    break;
                                self.sock.send(bytesToSend)
                elif filename == '/list':
                    files=''
                    for file in dirs:
                        files += file + ' - '
                    self.sock.send(files)
                elif filename == '/pwd':
                    self.sock.send(path)

                elif filename == '/cd':
                    self.sock.send('change')
                    new_path = self.sock.recv()
                elif filename == '/q':
                    self.sock.close()
                    break
                else:
                    self.sock.send('ERR')
            except RuntimeError:
                self.sock.close()
                break

def Main():
    TCP_IP = 'localhost'
    TCP_PORT = 5001

    s = MySocket.FullSocket()
    s.bind((TCP_IP, TCP_PORT))

    threads = []

    while True:
        s.listen(5)
        print "Waiting for incoming connections..."
        (conn, (ip,port)) = s.accept()
        c = MySocket.FullSocket(conn)
        print 'Got connection from ', (ip,port)
        newthread = ClientThread(ip,port,c)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()

if __name__ == '__main__':
    Main()
