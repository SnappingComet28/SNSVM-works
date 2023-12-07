from kivy.lang import Builder
from kivymd.app import MDApp
kivy = '''
MDBoxLayout:
    ScreenManager:
        id:screen
        Screen:
            name: "main"
            MDTopAppBar:
                pos_hint:{"top":1}
                title: "Hospital Interface"
                elevation:4
                md_bg_color: 240/255, 67/255, 55/254, 1
                center_title: True
                left_action_items: [["server"]]
            MDCard:
                padding:"20dp"
                size_hint:None,None
                radius:[48]
                elevation:4
                pos_hint:{"center_x":0.2,"center_y":0.5}
                md_bg_color:230/255, 225/255, 225/255,1
                size:350,300
                on_release :app.scanner()
                MDRelativeLayout:
                    Image:
                        source :"Capture.png"
                        size_hint:1,1
                        pos_hint:{"center_x":0.5,"center_y":0.5}
                    MDLabel:
                        text: "Scanner"
                        theme_text_color:"Primary"
                        pos_hint:{"center_x":0.9,"center_y":0.1}
        Screen:
            name: "error"
            MDTopAppBar:
                pos_hint:{"top":1}
                title: "Error"
                left_action_items:[["arrow-left",lambda x:app.schange("main")]]
            MDLabel:
                text:"Something went wrong most probably due to camera or network issue"
                pos_hint:{"center_x":0.8,"center_y":0.5}
        Screen:
            name: "Valid"
            MDTopAppBar:
                title:"validation"
                pos_hint:{"top":1}
            


'''
class App(MDApp):
    def build(self): 
        return Builder.load_string(kivy)
    def schange(self,screen1):
        self.root.ids.screen.current = screen1
    def scanner(self):
        self.schange("Valid")
        try:
            import cv2 
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            decoder = cv2.QRCodeDetector()
            while True:
                _,frame = cap.read()
                cv2.imshow("QR Scanner",frame)
                if cv2.waitKey(1) & 0xFF == ord('f'):
                    break
                output,_,_ = decoder.detectAndDecode(frame)
                if output:
                    self.check(output)
                    break
        except:
            self.schange("error")
        cap.release()
        cv2.destroyAllWindows()
    def check(self,output):
        from re import findall
        date = r"date: (\d+/\d+/\d+)"
        print(findall(date,output))
    
App().run()