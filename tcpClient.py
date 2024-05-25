from socket import *

serverName = 'soohians-MacBook-Air.local'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
# TCP needs to connect first, before sending
clientSocket.connect((serverName, serverPort))
message = input('Enter lowercase sentence:')

clientSocket.send(message.encode())

# recvfrom contains senderIP and port, but recv doesn't. Not needed since it's a connection
modifiedSentence = clientSocket.recv(1024) 
print('From server:', modifiedSentence.decode())
clientSocket.close()