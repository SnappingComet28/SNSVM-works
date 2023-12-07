import mysql.connector
import tkinter as tk
import threading as th

root = tk.Tk()
root.title("Chat!")

label = tk.Label(root, text="loading")
entry = tk.Entry(root)

label.pack()
entry.pack()

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chat"
)
cursor = database.cursor()

def receive():
    cursor.execute("SELECT ppl2 FROM chat WHERE id = 1")
    received = cursor.fetchone()
    label.config(text=received[0])
    database.commit()
    root.after(1000, receive) 
def send():
    msg = entry.get()
    query = 'UPDATE chat SET ppl1 = %s WHERE id = 1'
    cursor.execute(query, (msg,))
    database.commit()

button = tk.Button(root,text="Send!",command=send)
button.pack()
catch = th.Thread(target=receive)
catch.start()
root.mainloop()