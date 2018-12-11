import os
import socket



s = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.10.111'
#print(host)

port = 65432
s.bind((host, port))
s.listen()
print('server started')

#while True:

conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)    
        conn.sendall(data)




# s.listen(1)
# while True:
#     print('Server Started')
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#     c.close()
