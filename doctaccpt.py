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
cursor.execute("SELECT * FROM cardiac")
lists=str(cursor.fetchall())
data=[]
temp=""
closed = False
for letter in lists:
    if letter.isdigit():
        temp=temp+letter
    elif letter == ".":
        temp=temp+letter
    elif letter == ",":
        data.append(temp)
        temp = ""
    elif letter == ")":
        data.append(temp)
        temp = ""
    else:
        pass
ip = data[1]
port = data[2]
print("conntenting to patient")
doc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
doc.connect((ip,int(port)))
def recieve():
    while True:
        try:
            incoming = doc.recv(1024)
            if incoming:
                m = incoming.decode("utf-8")
                print(f"Server: {m}")
            else:
                pass
        except ConnectionResetError:
            print("Patient Left")
            break
    doc.close()
def send():
    while True:
        try:
            if closed == True:
                break
            msg = input("You: ")
            doc.send(msg.encode('utf-8'))
        except ConnectionResetError:
            print("Patient Left")
            break
    doc.close()
sending = threading.Thread(target=send)
recive = threading.Thread(target=recieve)
sending.start()
recive.start()