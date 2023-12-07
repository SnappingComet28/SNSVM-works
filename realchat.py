import socket
import threading
doc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
doc.connect(("localhost",12345))
def recieve():
    while True:
        try:
            incoming = doc.recv(1024)
            if incoming:
                m = incoming.decode("utf-8")
                print(f"Server: {m}")
            else:
                pass
        except:
            pass
def send():
    while True:
        msg = input("You: ")
        doc.send(msg.encode('utf-8'))
sending = threading.Thread(target=send)
recive = threading.Thread(target=recieve)
sending.start()
recive.start()