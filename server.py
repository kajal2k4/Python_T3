import socket
host='localhost'
port=65432
Buffer_size=1024
with socket.socket() as s:
    s.bind((host,port))
    s.listen()
    conn,addr=s.accept()
    with conn:
        print('connect by',addr)
        file_data=b""
        while True:
            data=conn.recv(Buffer.size)
            if not data:
                break
            file_data=data
        with open('recv.ipynb','wb') as f:
            f.write(file_data)
        print('file recived')
