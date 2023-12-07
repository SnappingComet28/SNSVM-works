from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from time import sleep
from kivy.clock import Clock
import sqlite3
kivy = '''
MDBoxLayout:
    ScreenManager:
        id:screen
        Screen:
            name:"login"
            MDTopAppBar:
                pos_hint: {'top': 1}
                title: "Login Page"
                elevation: 5
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
            MDLabel:
                text:"Please login Here"
                pos_hint:{"center_x":0.95,"center_y":0.8}
            MDTextFieldRect:
                id:user
                hint_text:"Enter Username"
                pos_hint:{"center_x":0.5,"center_y":0.7}
                size_hint:(0.4,0.05)
            MDTextFieldRect:
                id:phone
                hint_text:"Phone Number"
                pos_hint:{"center_x":0.5,"center_y":0.6}
                size_hint:(0.4,0.05)
            MDTextFieldRect:
                id:pin
                hint_text:"Enter password"
                size_hint:(0.4,0.05)
                password:True
                pos_hint:{"center_x":0.5,"center_y":0.5}
            MDRaisedButton:
                text:"Submit"
                pos_hint:{"center_x":0.5,"center_y":0.4}
                on_release: app.iscomplete()
        Screen:
            name: "main"
            MDBottomAppBar:
                MDTopAppBar:
                    MDIconButton:
                        icon : "home"
                        on_release:app.change_screen("main")
                        pos_hint:{"center_x":0.45}
            MDTopAppBar:
                pos_hint: {'top': 1}
                title: "XYZ Hospital"
                elevation: 5
                id: color
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                right_action_items: [["heart-plus"]]
            
            MDCard:
                padding:"20dp"
                size_hint:None,None
                radius:[48]
                elevation:4
                pos_hint:{"center_x":0.2,"center_y":0.6}
                md_bg_color:230/255, 225/255, 225/255,1
                size:350,300
                on_release :app.change_screen("choose")
                MDRelativeLayout:
                    MDLabel:
                        text:"Register"
                        theme_text_color : "Primary"
                        pos_hint:{"center_x":0.8,"center_y":0.9999}
                    Image:
                        source:"register.png"
                        pos_hint:{"center_x":0.5,"center_y":0.376}
                        size_hint : None,None
                        size:450,220
            MDCard:
                padding:"20dp"
                size_hint:None,None
                radius:[48]
                elevation:4
                pos_hint:{"center_x":0.5,"center_y":0.6}
                md_bg_color:230/255, 225/255, 225/255,1
                size:350,300
                on_release :app.change_screen("choose1")
                MDRelativeLayout:
                    MDLabel:
                        text:"Contact Doctor"
                        theme_text_color : "Primary"
                        pos_hint:{"center_x":0.7,"center_y":0.9999}
                    Image:
                        source:"msg.png"
                        pos_hint:{"center_x":0.5,"center_y":0.376}
            MDCard:
                padding:"20dp"
                size_hint:None,None
                radius:[48]
                elevation:4
                pos_hint:{"center_x":0.8,"center_y":0.6}
                md_bg_color:230/255, 225/255, 225/255,1
                size:350,300
                on_release :app.change_screen("order")
                MDRelativeLayout:
                    MDLabel:
                        text:"Order Medicine"
                        theme_text_color : "Primary"
                        pos_hint:{"center_x":0.8,"center_y":0.9999}
                    Image:
                        source:"Ord.png"
                        pos_hint:{"center_x":0.5,"center_y":0.39}
                        size_hint:None,None
                        size:450,220

'''
database=sqlite3.connect("signins.db")
cursor = database.cursor()
class app(MDApp):
    def build(self):
        return Builder.load_string(kivy)
    def change_screen(self,screen_name):
        self.root.ids.screen.current = screen_name
    def iscomplete(self):
        username = self.root.ids["user"].text
        phone = self.root.ids["phone"].text
        password = self.root.ids["pin"].text
        if username and phone and password:
            self.change_screen("main")
            cursor.execute(f'''INSERT INTO signins (username,password) VALUES ("{username}","{password}") ''')
        else:
            enterinfo = MDLabel(
                text="Error. Please Fill All Details.",
                pos_hint={"center_x":0.93,"center_y":0.3}
            )
            self.root.ids.screen.get_screen("login").add_widget(enterinfo)
            Clock.schedule_once(lambda dt:self.delenterinfo(enterinfo),3)
    def delenterinfo(self,label):
        self.root.ids.screen.get_screen('login').remove_widget(label)
app().run()