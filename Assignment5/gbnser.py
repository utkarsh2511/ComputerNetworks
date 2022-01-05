#!/usr/bin/python3
from socket import *
import threading
from sys import *
from os import *
from _thread import *
import random
import time
sndpkt = []
nextseqnum = 0
base = 0

global sendSock


lasttime = time.time()


def make_pkt(data):
	data = str(nextseqnum) + " " + str(data)
	return str(data)



def randomiser(data):
	global sendSock
	global nextseqnum
	if(random.choice([True, False, True, True])):
		sendSock.send(str(data).encode())
	print("Sender: sending packet " +  str(nextseqnum))

def timeout():
	global base
	global lasttime
	global nextseqnum
	currenttime = time.time()
	if(currenttime - lasttime > 2.0):
		lasttime = time.time()
		i = base
		while(i < nextseqnum):
			randomiser(str(sndpkt[i]))
			i += 1
				
		
def rdt_send(data, N):
	global sndpkt	
	global nextseqnum
	global base
	global lasttime
	if(nextseqnum < base + N):
		sndpkt.append(make_pkt(data))
		
		randomiser(str(sndpkt[nextseqnum]))
		if(base == nextseqnum):
			lasttime = time.time()
		nextseqnum += 1
		timeout()
		return True
	else:	
		timeout()
		return False
def rdt_sends(strings, length):
	i = 0
	
	while(i < len(strings)):
		if(i == 1):
			t2 = start_new_thread(rdt_rcv, ( ))
		if(rdt_send(strings[i], length)):
			i += 1
	while(True):
		pass

def getacknum(rcvpkt):
	return int(rcvpkt)

def rdt_rcv():
	global nextseqnum
	global base
	global lasttime
	global sendSock
	while True:
		rcvpkt = sendSock.recv(1024).decode()
		base = int(getacknum(rcvpkt)) + 1
		print("Sender: Acknowledgement recieved for packet " + str((base - 1))  )
		if(base == nextseqnum):
			pass
		else:
			lasttime = time.time()
def Main():
	global	sndpkt
	global	nextseqnum
	global	base
	global sendSock
	nextseqnum = 0
	base = 0
	Port1 = int(argv[2])
	connectionSock = socket(AF_INET, SOCK_STREAM)
	connectionSock.bind(('',Port1))
	connectionSock.listen(5)
	sendSock, addr = connectionSock.accept()

	strings = ["Hi", "bye", "who", "where", "when", "which", "why", "hello", "how", "what" ]
	N = int(argv[1])
	t1 = start_new_thread(rdt_sends, (strings, N))
	while True:
		pass
	
if __name__ == '__main__':
	Main()
		
