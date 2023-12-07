from kivymd.app import MDApp
from kivy.lang import Builder
kivy = '''
MDBoxLayout:
    ScreenManager:
        id: Screen
        Screen:
            name:"main"
            MDTopAppBar:
                pos_hint: {'top': 1}
                title: "XYZ Hospital"
                elevation: 5
                id: color
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
            
'''
class app(MDApp):
    def build(self):
        return Builder.load_string(kivy)
    def change_screen(self,screen):
        self.root.ids.screen.current = screen
app().run()