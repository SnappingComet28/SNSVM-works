import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",12345))
server.listen()
addrs = []
print(("server is started"))
def recieve(client):
    while True:
        msg = client.recv(1024)
        if msg:
            msg = msg.decode('utf-8')
            for addres in addrs:
                if addres != client:
                    addres.send(msg.encode('utf-8'))
        else:
            pass

while True:
    client,addr = server.accept()
    addrs.append(client)
    recive = threading.Thread(target=recieve,args=(client,))
    recive.start()