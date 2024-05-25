from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the port to the socket
serverSocket.bind(('', serverPort)) # tuple of address and port no.

while True:
    print('The server is ready to receive...')
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f'Message received from {clientAddress}, sending reply...')
    modifiedMessage = message.decode().upper()
    
    # UDP requires the client address and port for sending
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print('Reply sent.')

