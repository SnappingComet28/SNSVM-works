from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

kv = '''
ScreenManager:
    LoginScreen:
        name: 'login'
    MainScreen:
        name: 'main'

<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: username_field
            hint_text: "Enter Username"
        MDTextField:
            id: password_field
            hint_text: "Enter Password"
            password: True
        MDRaisedButton:
            text: "Login"
            on_release: app.check_credentials()

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Welcome to the Main Screen"
'''

class LoginScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def check_credentials(self):
        username = self.root.ids.login.ids.username_field.text
        password = self.root.ids.login.ids.password_field.text

        if username == 'admin' and password == 'password':
            self.root.current = 'main'
        else:
            self.show_error_message()

    def show_error_message(self):
        # Implement your error handling logic here
        print("Invalid credentials")

if __name__ == '__main__':
    MyApp().run()

