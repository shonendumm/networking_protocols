from socket import *
from time import localtime, strftime
import time

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
socket.settimeout(clientSocket, 1) # timeout of 1s


for i in range(10):
    try:
        time_sent = time.monotonic()
        msg = f"sequence_{i} { strftime('%c', localtime()) }"
        clientSocket.sendto(msg.encode(), (serverName, serverPort))
        recvMsg, serverAddress = clientSocket.recvfrom(1024)
        if recvMsg:
            time_recv = time.monotonic()
            rtt = time_recv - time_sent
            print(f"{recvMsg.decode()}, RTT: {rtt*1000: .2f} miliseconds")
        
    except timeout:
        print(f"sequence_{i} failed. Request timed out.")
        
