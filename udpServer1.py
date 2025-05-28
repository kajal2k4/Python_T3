import socket
host = socket.gethostname()
port = 5000
server_socket = socket.socket(type=socket.SOCK_DGRAM)
server_socket.bind((host,port))
while True:
    print('Waiting for message')
    data,addr = server_socket.recvfrom(1024)
    print('received'+data.encode(),addr)
    data = input('->')
    server_socket.sendto(msg.encode(),addr)
server_socket.close()
