import socket
import datetime

host = '0.0.0.0'
port = 3434

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    data, addr = s.recvfrom(1024)
    print(f'Received {data} from {str(addr)}')

s.close()
