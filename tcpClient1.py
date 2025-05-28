import socket
host = socket.gethostname()
port = 5000
client_socket = socket.socket(type=socket.SOCK_DGRAM)
ADDR= (host,port)
while True:
    data = input("-send")
    if not data:
        break
    client_socket.sendto(data.encode(),ADDR)
    print('received data')
    data,ADDR = client_socket.recvfrom(1024)
    if not data:
        break
    print("Recieved",data.decode())
client_socket.close()
