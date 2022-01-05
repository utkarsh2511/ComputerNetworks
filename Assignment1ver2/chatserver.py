#!/usr/bin/python3
from socket import *

from _thread import *
import threading

lock = threading.Lock()
def threading(c, addr):
	while True:
		try:
			data = c.recv(1024).decode()
			if data:
				#lock.release()
				print('client:', end = " ")
				print(addr[0], end = " ")
				print(':', end = " ")
				print(data)
				sentence = input('Server: ')
				c.send(sentence.encode())
		
			else:
				remove(c)
		except:
			continue

def remove(c):
	if c in list_of_clients:
		list_of_clients.remove(c)

def Main():
	serverPort = 12029
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind(('',serverPort))
	serverSocket.listen(50)
	print('The server is ready to receive')
	list_of_clients = []
		
	while True:
		connectionSocket, addr = serverSocket.accept()
		list_of_clients.append(connectionSocket)
		print (addr[0] + "connected")
		#lock.acquire()	
		start_new_thread(threading, (connectionSocket, addr,))

	connectionSocket.close()
	serverSocket.close()	

if __name__ == '__main__':
	Main()
