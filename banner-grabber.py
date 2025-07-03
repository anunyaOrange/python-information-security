import socket

s = socket.socket()

ip = "192.168.1.1"
port = "22"

s.connect((ip, int(port)))
print(s.recv(1024).decode())


