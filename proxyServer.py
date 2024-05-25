from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the port to the socket
serverSocket.bind(('', serverPort)) # tuple of address and port no.
serverSocket.listen(1)


while True:
    print('The server is ready to receive...')
    connectionSocket, clientAddress = serverSocket.accept() # serverSocket waits here, to create connectionSocket

    print(f'Connection established with {clientAddress}')
    message = connectionSocket.recv(1024).decode()
    print(f'Message received.')
    print(message)
    
    connectionSocket.close()
