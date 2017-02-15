#!/usr/bin/python

__author__ = 'Stefano Carone'
import threading

class Hosts:
    def __init__(self, ip, state=2):
        self.ip = ip
        self.state = state
        self.lock = threading.Lock()

    def ping(self, status, bot):
        self.lock.acquire()
        log = open('AliveHosts.log', 'a')
        if status != self.state:
                from time import gmtime, strftime
                if status == 0:
                        instant = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        txt = "{} {} Alive \n".format(instant, self.ip)
                        bot.sendMessage(chat_id=124490713, text=txt)
                        print txt
                else:
                        instant = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        txt = "{} {} Dead \n".format(instant, self.ip)
                        bot.sendMessage(chat_id=124490713, text=txt)
                        print txt
                log.write(txt)
                log.close()
        self.state = status
        self.lock.release()

## MAIN ##

def run( obj, trash):
    import telegram
    import subprocess
    bot = telegram.Bot(token="296505578:AAHV-r5TOb2s_HO_ggs4DdYlGttUnIAeW08")
    global dead
    while not dead:
        cmd = ('ping', str(obj.ip), '-c', '1', '-W', '1')
        err = subprocess.call(cmd, stderr = trash, stdout = trash)
        obj.ping(int(err), bot)

def main():
    import threading
    from time import gmtime, strftime
    global dead
    dead = False
    with open('hosts.txt', 'r+') as file:
        listaHosts = file.readlines()
    cestino = open('/dev/null', 'w')
    listaClasse = []
    for i in range(len(listaHosts)):
            objHost = Hosts(listaHosts[i].strip('\n'))
            listaClasse.append(objHost)
    with open('AliveHosts.log', 'w') as file:
            instant = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            txt = "{} --> StartLog\n".format(instant)
            file.write(txt)
    for h in listaClasse:
            t = threading.Thread(target = run, args = (h,cestino,))
            t.start()

    raw_input(" ")
    dead = True
    with open('AliveHosts.log', 'a') as file:
        instant = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        txt = "{} --> endLog\n".format(instant)
        file.write(txt)

if __name__ == "__main__":
    main()

