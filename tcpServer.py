from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the port to the socket
serverSocket.bind(('', serverPort)) # tuple of address and port no.
serverSocket.listen()

while True:
    print('The server is ready to receive...')
    connectionSocket, clientAddress = serverSocket.accept()
    print(f'Connection established with {clientAddress}')

    message = connectionSocket.recv(1024)
    print(f'Message received, sending reply...')
    modifiedMessage = message.decode().upper()
    
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
    print('Reply sent.')