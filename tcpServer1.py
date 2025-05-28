from socket import *

server = socket()
server.bind(('localhost',90000))
server.listen()
while(1):
    (client,add) = server.accept()
    rd = client.recv(1028).decode()
    print(rd)
    data = "HTTP/11 200 ok\r\n"
    data += "content-Type:text/html;charset=utf-8\r\n"
    data += "<html><body>Hello World</body></html\r\n\r\n>"
    client.send(data.encode())
server.close()
print("http://localhost:9000")
