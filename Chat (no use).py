from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from datetime import datetime
import socket
import threading

style = """
MDBoxLayout:
    orientation: "vertical"
    ScreenManager:
        id: screen
        Screen:
            name: "main"
            MDTopAppBar:
                pos_hint: {"top": 1}
                title: "Home"
                left_action_items: [["home"]]
            MDFloatLayout:
                MDRoundFlatIconButton:
                    icon: "chat"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    text: "Recent Chat Requests"
                    md_bg_color: 98/255, 212/255, 100/255, 1
                    pos_hint: {"center_x": 0.3, "center_y": 0.6}
                    size_hint: 0.4, 0.1
                    on_release: app.change_screen("request")
        Screen:
            name: "chat_room"
            MDBoxLayout:
                orientation: "vertical"
                md_bg_color: 229/255, 235/255, 148/255, 1
                ScrollView:
                    MDBoxLayout:
                        orientation: "vertical"
                        id: chat_msg
                        spacing: "20dp"
                        adaptive_height: True
                MDRelativeLayout:
                    size_hint: 1, 0.19
                    MDTextFieldRect:
                        hint_text: "Message"
                        size_hint: None, None
                        size: 1200, 60
                        id: message_box
                        pos_hint: {"center_x": 0.5, "center_y": 0.19}
                    MDIconButton:
                        icon: "send"
                        md_bg_color: 15/255, 148/255, 117/255, 1
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        pos_hint: {"center_x": 0.85, "center_y": 0.19}
                        on_release: app.send()
        Screen:
            name: "request"
            MDTopAppBar:
                pos_hint: {"top": 1}
                title: "RECENT CHAT REQUESTS"
            MDFloatLayout:
                id: recent
"""

class app(MDApp):
    def build(self):
        return Builder.load_string(style)

    def change_screen(self, screen_name):
        self.root.ids.screen.current = screen_name

    def request1(self):
        host = 'localhost'
        port = 12345
        c_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_server.connect((host, port))
        while True:
            try:
                req = c_server.recv(1024)
                if req:
                    msg = req.decode('utf-8')
                    if msg == "ReQuEst":
                        self.temp()
                        break
                    else:
                        pass
                else:
                    pass
            except:
                pass

    def recive(self):
        while True:
            try:
                chat_data = self.c_server.recv(1024)
                if chat_data:
                    chat_msg = chat_data.decode('utf-8')
                    word1 = 1
                    for word in chat_msg:
                        if word.isalpha() or word.isspace():
                            word1 += 1
                        if word1 < 23:
                            height1 = 80
                        if word1 > 23:
                            height1 = word1 * 2
                    msg2 = MDLabel(
                        text=chat_msg,
                        size_hint_y=None,
                        theme_text_color=("Custom"),
                        text_color=(1, 1, 1, 1),
                        pos_hint={"center_x": 0.2, "center_y": 0.5},
                        padding=(15, 10)
                    )
                    doctor_msg = MDCard(
                        size_hint=(None, None),
                        size=(500, height1),
                        elevation=4,
                        pos_hint={"left": 0.98, "center_y": 0.3},
                        md_bg_color=(1, 1, 1, 1),
                        radius=[30],
                        size_hint_y=None
                    )
                    doctor_box = self.root.ids.chat_msg
                    doctor_msg.add_widget(msg2)
                    doctor_box.add_widget(doctor_msg)
                else:
                    pass
            except:
                pass

    def chat(self):
        self.change_screen("chat_room")
        recive_msg = threading.Thread(target=self.recive)
        recive_msg.start()

    def temp(self):
        tem = self.root.ids.recent
        btn = MDRaisedButton(
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.3, "center_y": 0.2},
            md_bg_color=(143/255, 81/255, 194/255, 1),
            on_release=self.chat
        )
        tem.add_widget(btn)

    def send(self):
        msg = self.root.ids["message_box"].text
        letter1 = 1
        if self.c_server and msg:
            for letter in msg:
                if letter.isalpha() or letter.isspace():
                    letter1 += 1
                if letter1 < 23:
                    height = 80
                if letter1 > 23:
                    height = (letter1) * 2
            if msg:
                msg1 = MDLabel(
                    text=msg,
                    size_hint_y=None,
                    theme_text_color=("Custom"),
                    text_color=(1, 1, 1, 1),
                    pos_hint={"center_x": 0.2, "center_y": 0.5},
                    padding=(15, 10)
                )
                current_time = datetime.now().strftime("%I : %M %p ")
                current_time1 = MDLabel(
                    text=current_time,
                    theme_text_color="Secondary",
                    pos_hint={"center_x": 1.4, "center_y": 0.4},
                    size_hint=(1, 1)
                )
                chat_box = self.root.ids.chat_msg
                chat1 = MDCard(
                    size_hint=(None, None),
                    size=(500, height),
                    elevation=4,
                    pos_hint={"right": 0.98, "center_y": 0.3},
                    md_bg_color=(66 / 255, 154 / 255, 227 / 255, 1),
                    radius=[30],
                    size_hint_y=None
                )
                chat1.add_widget(msg1)
                chat_box.add_widget(chat1)
                chat_box.add_widget(current_time1)
                self.root.ids["message_box"].text = ""
                self.c_server.send(msg.encode('utf-8'))
            elif msg == "":
                pass
        else:
            pass

app().run()