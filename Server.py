import threading as th
import socket

clients = []
class hosapp():
    def chat(self):
        host = "192.168.29.86"
        port = 12345
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(5)
        print("server is running")
        while True:
            try:
                client_socket , addr =  server.accept()
                clients.append(client_socket)
                
                recive_thread = th.Thread(target=self.recive, args=(client_socket))
                recive_thread.start()
            except:
                pass   
    
    def send(self, msg):
        for client in clients:
            if client!=self.client_socket:
                client_socket.send(msg.encode("utf-8"))
            else:
                pass
    def recive(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if data:
                    msg = data.decode('utf-8')
                    print(msg)
                    self.send(msg=msg)
                else:
                    pass
            except:
                pass
        
    def run(self):
        self.chat()

hosapp().run()
