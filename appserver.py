import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("192.168.29.86",12345))
server.listen()
addrs = []
print(("server is started"))
def recieve(client):
    while True:
        try:
            msg = client.recv(1024)
        except ConnectionResetError:
            client.close()
        if msg:
            msg = msg.decode('utf-8')                
            for addres in addrs:
                if addres != client:
                    try:
                        addres.send(msg.encode('utf-8'))
                    except ConnectionResetError as e:
                        addrs.remove(addres)
        else:
            pass

while True:
    client,addr = server.accept()
    addrs.append(client)
    recive = threading.Thread(target=recieve,args=(client,))
    recive.start()