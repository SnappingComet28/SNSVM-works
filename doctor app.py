from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from time import sleep
import threading as th
import  socket
from kivymd.uix.card import MDCard
from kivy.clock import Clock
kivy = ''' 
MDBoxLayout:
    ScreenManager:
        id:screen
        Screen:
            name:"main"
            MDTopAppBar:
                pos_hint: {'top':1}
                title: "Doctor Interface"
                elevation:3
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
                right_action_items: [["heart-plus"]]
            MDCard:
                padding:"20dp"
                size_hint:None,None
                radius:[48]
                elevation:4
                pos_hint:{"center_x":0.2,"center_y":0.6}
                md_bg_color:230/255, 225/255, 225/255,1
                size:350,300
                on_release :app.change_screen("accept")
                MDRelativeLayout:
                    MDLabel:
                        text:"Requests"
                        theme_text_color : "Primary"
                        pos_hint:{"center_x":0.8,"center_y":0.9999}
                    Image:
                        source:"requests.png"
                        pos_hint:{"center_x":0.5,"center_y":0.376}
                        size_hint : None,None
                        size:450,220
        Screen:
            name: "accept"
            MDTopAppBar:
                pos_hint: {'top':1}
                title: "Requests"
                elevation:3
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
                right_action_items: [["heart-plus"]]
                left_action_items:[["arrow-left", lambda x : app.change("main")]]
            MDRelativeLayout:
                id:temp
        Screen:
            name:"chatroom"
            MDBoxLayout:
                orientation: "vertical"
                md_bg_color : 229/255, 235/255, 148/255,1
            
                ScrollView:
                    MDBoxLayout:
                        orientation: "vertical"
                        id: chat
                        spacing: "20dp"
                        adaptive_height: True
                MDRelativeLayout:
                    size_hint: (1, 0.15)
                    MDTextFieldRect:
                        hint_text: "message"
                        size_hint: None, None
                        size: 1200, 60
                        id: message                        
                        pos_hint: {"center_x": 0.5, "center_y": 0.19}


'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(("localhost",12345))
class App(MDApp):
    def build(self):
        return Builder.load_string(kivy)
    def change_screen(self,name):
        self.root.ids.screen.current = name
    def recieve(self):
        while True:
            try:
                mess = server.recv(1024)
                if mess:
                    mesg1 = mess.decode("utf-8")
                    Clock.schedule_once(lambda dt: self.update_chat(mesg1))
            except:
                pass

    def update_chat(self, mesg1):
        letter2 = 1
        msg = mesg1
        for letter3 in msg:
            if letter3.isalpha() or letter3.isspace():
                letter2 += 1
            if letter2 < 23:
                height = 80
            if letter2 > 23:
                height = letter2 * 2

        msg2 = MDLabel(
            text=msg,
            size_hint_y=None,
            theme_text_color=("Custom"),
            text_color=(1, 1, 1, 1),
            pos_hint={"center_x": 0.2, "center_y": 0.5},
            padding=(15, 10),
        )
        current_time = datetime.now().strftime("%I : %M %p ")
        current_time3 = MDLabel(
            text=current_time,
            theme_text_color="Secondary",
            pos_hint={"center_x": 0.15, "center_y": 0.35},
            size_hint=(1, 1),
        )
        chat_box2 = self.root.ids.chat
        chat3 = MDCard(
            size_hint=(None, None),
            size=(500, height),
            elevation=4,
            pos_hint={"left": 0.98, "center_y": 0.3},
            md_bg_color=(66 / 255, 154 / 255, 227 / 255, 1),
            radius=[30],
            size_hint_y=None,
        )
        chat3.add_widget(msg2)
        chat_box2.add_widget(chat3)
        chat_box2.add_widget(current_time3)
    def send(self):
        msg = self.root.ids["message"].text
        if msg:
            msg1 = MDLabel(
                text=msg,
                size_hint_y=None,
                theme_text_color=("Custom"),
                text_color=(1, 1, 1, 1),
                pos_hint={"center_x": 0.2, "center_y": 0.5},
                padding=(15, 10),
            )
            current_time = datetime.now().strftime("%I : %M %p ")
            current_time1 = MDLabel(
                text=current_time,
                theme_text_color="Secondary",
                pos_hint={"center_x": 1.4, "center_y": 0.4},
                size_hint=(1, 1),
            )
            chat_box = self.root.ids.chat
            chat1 = MDCard(
                size_hint=(None, None),
                size=(500, 80),
                elevation=4,
                pos_hint={"right": 0.98, "center_y": 0.3},
                md_bg_color=(66 / 255, 154 / 255, 227 / 255, 1),
                radius=[30],
                size_hint_y=None,
            )
            chat1.add_widget(msg1)
            chat_box.add_widget(chat1)
            chat_box.add_widget(current_time1)
            server.send(msg.encode("utf-8"))
            self.root.ids["message"].text = ""
    def accpet(self,dt):
        try:
            r=server.recv(1024)
            if r:
                re = r.decode(("utf-8"))
                if re =="__ReQuEsT__":
                    req = MDCard(MDLabel(text="Accpet request"),on_release=self.request())
                    self.root.ids.accept.add_widget(req)
                else:
                    pass
        except:
            pass
    def request(self):
        server.send("__AcCpEcT__".encode("utf-8"))
        sleep(1)
        self.change_screen("chat_room")
        re = th.Thread(target=self.recieve)
        re.start()
    def on_start(self):
        Clock.schedule_interval(self.accpet, 1)
App().run()