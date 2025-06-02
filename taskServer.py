#SERVER
import socket
host=socket.gethostname()
port=5000
server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen()
conn,address=server_socket.accept()
print("Connection from :",str(address))
while True:
    data=conn.recv(1024).decode()
    s=s.split(" ")
    ans=""
    for i in s:
        if int(i)%2==1:
            ans=ans+int(i)**3+" " 
    if not data:
        break
    print("from connected user:",str(data))
    conn.send(ans.encode())
conn.close()
