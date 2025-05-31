import socket
port = 5000
client_socket = socket.socket()
client_socket.connect((192.168.104.31,port))
message = input('->')
while message.lower().strip()!='bye':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print('received from server'+data)
    message = input('->')
client.socket.close()


