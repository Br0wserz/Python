#!/usr/bin/python

__author__ = 'Stefano Carone'

import telegram
import threading
from time import gmtime, strftime
import subprocess

global lock, dead, bot
lock = threading.Lock()
dead = False

class Hosts:
    def __init__(self, ip, state=2):
	self.ip = ip
	self.state = state

    def ping(self,status):
	global lock, bot
        lock.acquire()  
	log = open('AliveHosts.log','a')
	if status != self.state:
		if status == 0:
			now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			string = "{} {} Alive \n".format(now,self.ip)
			bot.sendMessage(chat_id = 124490713, text = string)
			print string
		else:
			now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			string = "{} {} Dead \n".format(now,self.ip)
			bot.sendMessage(chat_id = 124490713, text = string)
                	print string
		log.write(string)
		log.flush()
		log.close()
        self.state = status
	lock.release()  

## MAIN ##

def main(obj,trash):
    global bot
    bot = telegram.Bot(token="308937285:AAGki0QsC0JmWMFFX7hDq_ZI0UTiKALOsKo")
    global dead
    while not dead:
	cmd = ('ping',str(obj.ip),'-c','1','-W','1')
	err = subprocess.call(cmd, stderr = trash, stdout = trash)
	obj.ping(int(err))

if __name__ == "__main__":
	with open('hosts.txt','r+') as file:
		listaHosts = file.readlines()
	cestino = open('/dev/null','w')
	listaClasse = []
	for i in range(len(listaHosts)):
		objHost = Hosts(listaHosts[i].strip('\n'))
		listaClasse.append(objHost)
	with open('AliveHosts.log','w') as file:
		now = strftime("%Y-%m-%d %H:%M:%S", gmtime()) 
		string = "{} --> StartLog\n".format(now)
		file.write(string);
	for h in listaClasse:
		t = threading.Thread(target = main, args = (h,cestino,))
		t.start()

	raw_input (" ")
	dead = True	
        with open('AliveHosts.log','a') as file:
                now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                string = "{} --> endLog\n".format(now)
                file.write(string);

