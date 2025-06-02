import socket

host = "localhost"
port = 65432
Buffer_size = 1024
with Socket.socket() as s:
    s.connect((host,port))
    with open('Lec-1.ipynb','rb') as f:
        while True:
            data = f.read(Buffer_size)
            if not data:
                break
            s.sendall(data)
        print('file send')
