from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import socket
import threading as th
from kivymd.uix.card import MDCard
from datetime import datetime

style = '''
Screen:
    name:"chatroom"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 229/255, 235/255, 148/255, 1

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
            MDIconButton:
                icon: "send"
                pos_hint: {"center_x": 0.97, "center_y": 0.19}
                on_release: app.send()

'''
try:
    user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user.connect(("192.168.29.86", 12345))
except Exception as e:
    print(f"Connection error: {e}")

class app(MDApp):
    def build(self):
        return Builder.load_string(style)

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
            user.send(msg.encode("utf-8"))
            self.root.ids["message"].text = ""

    def reading(self, *args):
        while True:
            try:
                messg = user.recv(1024)
                if messg:
                    msg1 = messg.decode("utf-8")
                    Clock.schedule_once(lambda dt: self.update_chat(msg1))
            except Exception as e:
                print(f"Error in reading thread: {e}")

    def update_chat(self, msg):
        letter2 = 1
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

    def on_start(self):
        rec = th.Thread(target=self.reading)
        rec.start()


if __name__ == "__main__":
    app().run()
