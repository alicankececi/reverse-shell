import os
import subprocess
import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname()) 
port = 9999

s.connect((host,port))


while True:
    cmd = input()
    if cmd == 'quit':
        s.close()
        sys.exit()
    if len(str.encode(cmd)) > 0: 
        s.send(str.encode(cmd)) 
        server_response = str(s.recv(1024),"utf-8") 
        print(server_response, end="")
