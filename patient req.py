import mysql.connector
import socket
import threading
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="requests"
)
cursor = database.cursor()
closed = False
def exip():
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    return ip
ip = exip()
cursor.execute(f'''INSERT INTO cardiac (ip,port) VALUES ("{ip}",12345)''')
database.commit()
print("Cardiac request sent sucessfully")
print("Waiting for someone...")
def startserver():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,12345))
    server.listen()
    addrs = []
    print(("server is started"))
    def recieve(client):
        global closed
        if closed != True:
            while True:
                try:
                    msg = client.recv(1024)
                    if msg:
                        msg = msg.decode('utf-8')
                        for addres in addrs:
                            if addres != client:
                                addres.send(msg.encode('utf-8'))
                    else:
                        pass
                except ConnectionResetError:
                    print("Doct disconnected")
                    break
        server.close()
        closed = True

    while True:
        client,addr = server.accept()
        addrs.append(client)
        recive = threading.Thread(target=recieve,args=(client,))
        recive.start()
def chat():
    server = threading.Thread(target=startserver)
    server.start()
    doc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    doc.connect((ip,12345))
    def recieve():
        global closed
        if closed!= True:
            while True:
                try:
                    incoming = doc.recv(1024)
                    if incoming:
                        m = incoming.decode("utf-8")
                        print(f"Server: {m}")
                    else:
                        pass
                except ConnectionRefusedError:
                    print("Doct left")
            server.close()
            closed = True
    def send():
        global closed
        if closed != True:
            while True:
                try:
                    if closed == True:
                        break
                    msg = input("You: ")
                    doc.send(msg.encode('utf-8'))
                except ConnectionResetError:
                    print("Doct left")
                    break    
        server.close()
        closed = True
    sending = threading.Thread(target=send)
    recive = threading.Thread(target=recieve)
    sending.start()
    recive.start()
chat()