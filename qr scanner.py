import cv2 
from datetime import datetime,timedelta
decoder = cv2.QRCodeDetector()
img = cv2.imread("qrcode.png")
text,_,_ = decoder.detectAndDecode(img)
_,waste,time,waste1 = text.split("!")
time = time.replace("time:","")
def ctime():
    now = datetime.now()
    one_day_ahead = now + timedelta(seconds=1)
    time = one_day_ahead.strftime("%d %H")
    return time
if time == ctime():
    print("valid")
else:
    print("invalid")