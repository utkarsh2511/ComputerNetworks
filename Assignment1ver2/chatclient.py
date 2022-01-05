#!/usr/bin/python3
from socket import *
serverName = '127.0.0.1'
serverPort = 12029
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
	sentence = input('client: ')
	clientSocket.send(sentence.encode())
	print("server:", end = " ")
	print(clientSocket.recv(1024).decode())
	
clientSocket.close()
	
