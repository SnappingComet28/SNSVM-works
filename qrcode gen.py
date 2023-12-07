import qrcode as qr
from datetime import datetime,timedelta
from time import asctime
data = {}
name = input("Enter name: ")
age = input("Enter age: ")
time = input("Today or tomorrow?: ")
if time == "tomorrow":
    now = datetime.now()
    one_day_ahead = now + timedelta(days=1)
    time = one_day_ahead.strftime("%d %H")
elif time == "today":
    now = datetime.now()
    one_day_ahead = now + timedelta(seconds=1)
    time = one_day_ahead.strftime("%d %H")
data["name"] = name
data["age"] = age
data["time"] = time
data1 = ""
for key,value in data.items():
    data1=data1+(f"{key}:{value}!")
print(data1)
img = qr.make(data1)
img.save("qrcode.png")
