import socket, struct

host = 'url'
port = 80

# TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((host,port))
total = 0

while 1:
    data = s.recv(4)
    print data
    s.send()
s.close()