import imp
import time

MySocket = imp.load_source('Fullsocket', r"C:\Users\Stefano\PycharmProjects\RetrFile\libs\FullSocket")

def Main():

    host = '127.0.0.1'      # The remote host
    port = 5001          # The same port as used by the server

    sock = MySocket.FullSocket()
    sock.connect((host, port))
    stop = True
    while stop == True:
       filename = raw_input('Filename? -> ')
       if filename != '/q' and filename != '/list' and filename != '/pwd' and filename[:3] != '/cd' and filename != '/help':
           sock.send(filename)
           data = sock.recv()
           if data[:6] == 'EXISTS':
               filesize = long(data[6:])
               message = raw_input('File Exists, ' + str(filesize) + 'Bytes, download? (Y/N)? -> ')
               if message == 'Y':
                   sock.send('OK')
                   f = open('new_'+filename, 'wb')
                   totalRecv = 0
                   start = time.time()
                   while totalRecv < filesize:
                       data = sock.recv()
                       totalRecv += len(data)
                       f.write(data)
                       print'{0:.3f}'.format((totalRecv/float(filesize))*100) + '% Done'
                   time.sleep(1)
                   stop = time.time()
                   tempo = stop - start
                   vel = (totalRecv/1024)/tempo
                   print 'Download Complete! {0:.2f}'.format(vel) + ' KBytes/sec'
                   stop = True
               else:
                   sock.send('ERR')
           else:
               print 'File does not Exist!'
       elif filename == '/help':
            print '''
/list --> Visualizzare i files
/pwd --> Visualizzare il percorso
/cd (NewPath) --> Cambiare il percorso
/q --> Chiudere la connessione
            '''
       elif filename == '/list':
            sock.send(filename)
            data = sock.recv()
            print data
       elif filename == '/pwd':
            sock.send(filename)
            data = sock.recv()
            print data
       elif filename[:4] == '/cd ':
            sock.send(filename[:3])
            data = sock.recv()
            msg = filename[4:]
            msg += '/'
            sock.send(msg)
       elif filename == '/q':
            sock.send(filename)
            sock.close()
            stop = False


if __name__ == '__main__':
    Main()
