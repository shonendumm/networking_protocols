from socket import *
import sys

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen()

while True:
    print('Ready to serve...')
    connectionSocket, clientAddress = serverSocket.accept()
    print(f'Connection established with {clientAddress}')

    try:
        message = connectionSocket.recv(1024).decode()
        print(f"Received {message}")
        filename = message.split()[1] # split 'GET /helloworld.html'

        print(f"looking for {filename}")
        with open(filename[1:], 'r') as f: # omit the / in /helloworld.html
            outputdata = f.read()
        
        # Send http headers
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())

        # Encode and send the html data
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        print("File sent!")

        connectionSocket.close()
    
    # For file not found error
    except IOError: 
        print("Invalid filename, sending 404 response")
        response = ("HTTP/1.1 404 Not Found\r\n"
                    "Connection: close\r\n"
                    )
        connectionSocket.send(response.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
