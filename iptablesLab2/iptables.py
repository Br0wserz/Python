#!/usr/bin/python2.7

import csv
import time
import commands
import os
import argparse

class iptables:

	def __init__(self,op,chain,prot,port,subnet,name):
		if op == "ins":
			self.op = "I"
		elif op == "del":
			self.op = "D"
		elif op == "add":
			self.op = "A"
		self.name = name
		self.prot = prot
		self.port = port
		self.chain = chain
		self.subnet = subnet
	def runningCmd(self):
		self.NAKEDrULE = 'iptables -{0} {1} --protocol {2} --dport {3} -s {4} -j DROP'.format(self.op, self.chain, self.prot, self.port, self.subnet)
		Err = self.checkRule()
		if Err == 100:
			os.system(self.NAKEDrULE)
			os.system('iptables -{0} {1} -s {2} -p {3} --dport {4} -j LOG --log-prefix "{5}"'.format(self.op,self.chain,self.subnet,self.prot,self.port,self.name))
		elif Err == 101:
			self.logError()

	def checkRule(self):
		CHECKrULE = 'sudo iptables -C {0} --protocol {1} --dport {2} -s {3} -j DROP'.format(self.chain, self.prot, self.port, self.subnet)
		checkError = commands.getstatusoutput(CHECKrULE)
		if checkError[0] == 0 and self.op == "D":
			return 100
		elif checkError[0] != 0 and self.op == "I":
			return 100
		elif checkError[0] != 0 and self.op == "A":
			return 100
		else:
			return 101 
	def logError(self):
		timeError = time.strftime("%Y-%m-%d ")
		if self.op == "I" or self.op == "A":
			errore = "regola presente: "
		elif self.op == "D":
			errore = "regola assente: "
		errStr = timeError +  errore + self.NAKEDrULE + "\n" 
		with open('iptablesLab.log', 'a') as f:
			f.write(errStr)

def csvReader(f):
	reader = csv.reader(f)
	nakedList = []
	for row in reader:
		nakedList.append(row)
	return nakedList
def decompose_nakedList(iptab,nakedList):
	prot = 'tcp'
	for row in nakedList:
		iptab.append(iptables(row[0],row[2],prot,row[4],row[3],row[1]))
def run(iptab):
	for i in range(len(iptab)):
		iptab[i].runningCmd()
def sudo():
	import os
	import sys
	os.system("sudo -k")
	euid = os.geteuid()
	if euid != 0:
    		print "Script not started as root. Running sudo.."
    		args = ['sudo', sys.executable] + sys.argv + [os.environ]
	        os.execlpe('sudo', *args)

	print 'Running... \n Please view your new rule in the iptable'

sudo()
def args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action='store', dest='filerule',
                    help='choose name file.csv')
	results = parser.parse_args()
	if results.filerule == None:
		os.system("sudo iptables -L")
	else:
		return results.filerule
filerule = args()
try:
	with open(filerule,'r') as file:
		ruleList = csvReader(file)
	arrayObj = []
	decompose_nakedList(arrayObj,ruleList)
	run(arrayObj)

except TypeError:
	print
