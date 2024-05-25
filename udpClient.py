from socket import *

serverName = 'soohians-MacBook-Air.local'
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET = IPv4
    message = input('Input lowercase sentence:')

    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

    clientSocket.close()
