import socket

host = '127.0.0.1'
port = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'Hello World'
s.sendto(data.encode('utf-8'), (host, port))
s.close()
