import socket
import threading as th

class user():
    def chat(self):
        host = "192.168.1.35"
        port = 12345
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            server.connect((host,port))
        except:
            print("refused connection")
        
    def recive(self):
        while True:
            try:
                data = self.server.recv(1024)
                if data:
                    msg = data.decode('utf-8')
                    print(msg)
                else:
                    pass
            except:
                pass
    def send(self):
        while True:
            msg1 = input("enter the msg :")
            try:
                self.server.send(msg1.encode('utf-8'))
            except:
                pass

    def run(self):
        self.chat()

user().run()
