import socket
user = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
user.connect(("192.168.29.86",12345))
while True:
    user.send(input("You: ").encode('utf-8'))
