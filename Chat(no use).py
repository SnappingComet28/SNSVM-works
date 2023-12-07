from kivymd.app import MDApp
from kivy.lang import Builder
import threading
import re
import socket

style ="""
MDBoxLayout:
	orientation:"vertical"
	ScreenManager:
		id : screen
		Screen:
			name:"main"
			MDTopAppBar:
				title :"SERVER"
				pos_hint:{"top":1}
				left_action_items : [["server"]]

"""
clients =[]
class server(MDApp):
	
	def build(self):
		return Builder.load_string(style)
	def send_msg(self,msg,c_server):
		for client in clients:
			if client != c_server:
				try:
					client.send(msg.encode('utf-8'))
				except:
					pass
	def save_code(self,msg):
		with open("file.txt", "a") as file:
			file.write(msg + "\n")
	def recive(self,c_server):
		while True:
			try:
				data = c_server.recv(1024)
				if data:
					msg = data.decode('utf-8')
					match = re.match(r'\\(/d{4})\\',msg)
					if match:
						save_code(msg)
					elif not match:
						send_msg(msg,c_server)
				elif data =="":
					pass
			except:
				pass
	def on_start(self):
		host = 'localhost'
		port = 12345
		
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((host, port))
		server.listen()
		while True:
			c_server, addr = server.accept()
			clients.append(c_server)
			recive = threading.Thread(target=self.recive, args=(c_server,))
			recive.start()
	
server().run()