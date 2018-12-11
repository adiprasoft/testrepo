import socket

s = socket.socket()

host = '192.168.10.111'
port = 65432

s.connect((host,port))
s.sendall('Hello World, Having a fun day?')
print(s.recv(1024))
s.close