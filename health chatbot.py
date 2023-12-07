##not completed yet 💀

import tkinter as tk
from time import sleep as delay
root = tk.Tk()
root.title("health chatbot")
entry = tk.Entry(root)
def printtk(args):
    label.config(text=args)
    delay(1.5)
rprint = print
printtk = print
def doctor():
    print("Feature coming soon...")
def OSubmitted():
    global entry
    issue = entry.get()
    entry.pack_forget()
    print("If you want to consult a doctor then please let us know")
    yes = tk.Button(root,text="Yes please",command=doctor)
    yes.pack()
    no = tk.Button(root,text="No thanks",command=no.pack_forget())
    no.pack()
    print("Okay. A doctor will soon msg you. We advice you to take rest and drink water. ")
def other():
    print("Please briefly describe your issue.")
    entry.pack()
    button  = tk.Button(root,text="Submit",command=OSubmitted)
    entry.pack()
    button.pack()
label = tk.Label(root,text="Describe Your Situation")
label.pack()
button = tk.Button(root,text="other",command=other)
button.pack()
root.mainloop()
