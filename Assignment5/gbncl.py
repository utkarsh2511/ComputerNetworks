#!/usr/bin/python3
import threading
from sys import *
from os import *
from _thread import *
import random
from socket import *
expectedseqnum = 0
global rcvSock
sndpkt = "0 0"

def hasseqnum(rcvpkt):
	global expectedseqnum
	rcp = rcvpkt.split()
	num = str(rcp[0])
	if(num == str(expectedseqnum)):
		return True
	else:
		return False
		
		
def make_pkt():
	global expectedseqnum
	data = str(expectedseqnum)
	return data

def extract(rcvpkt):
	rcp = rcvpkt.split()
	return rcp[1]

def randomiser(data):
	global rcvSock
	if(random.choice([True, False, True, True])):
		rcvSock.send(data.encode())

def rdt_rcv():
	global sndpkt
	global rcvSock
	global expectedseqnum
	while True:
		rcvpkt = rcvSock.recv(1024).decode()
		
		if(hasseqnum(rcvpkt)):
			data = extract(rcvpkt)
			print(data)
			sndpkt = make_pkt()
			randomiser(sndpkt)
			expectedseqnum += 1
		else:		
			randomiser(sndpkt)
		
def Main():
	global expectedseqnum
	global rcvSock
	global rcvSock
	global sndpkt
	clientName = argv[1]
	Port1 = int(argv[2])
	
	rcvSock = socket(AF_INET, SOCK_STREAM)
	rcvSock.connect((clientName,Port1))
	rdt_rcv()

		


if __name__ == '__main__':
	Main()
