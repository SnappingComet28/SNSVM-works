import tkinter as tk
import dropbox as dbx
from time import sleep as sp
root=tk.Tk()
root.title("CHat!")
db = dbx.Dropbox("sl.BqBZszXdRrDTOcUaC8duoMxf2uvDx0q-zoZMGqARfhNRUbbPrKPOs_sY2IIaKP4pTwyLJaOuwZIBwq4_LqeU5aTN9BZNZJqNN4UOJzHR8r3eEeoAkD0uX5lxTL0RzBYbjmaaOprBiV4R",app_key="i5amtpv10b3grq2",app_secret="zpwazu18shjtdin")
file_path = "/test/dropbox.txt"
#dropbox below
def reading():
    try:
        # Download the file directly as bytes
        metadata, response = db.files_download(file_path)
        content = response.content

        # Decode the content from bytes to string (assuming it's a text file)
        content_str = content.decode('utf-8')

        # Now 'content_str' contains the text content of the file
        return content_str

    except dbx.exceptions.HttpError as e:
        print(f"Error With chat system:\n{e}")
        sp(3)
def send():
    global entry
    msg = entry.get()
    sending(msg)
def sending(msg):
    try:
        # Read the existing content of the file
        metadata, response = db.files_download(file_path)
        existing_content = response.content.decode('utf-8')

        # Modify the content as needed
        new_content = msg

        # Upload the modified content as a new version of the file
        db.files_upload(new_content.encode('utf-8'), "/test/ppl2.txt", mode=dbx.files.WriteMode('overwrite'))
        sp(1)

    except dbx.exceptions.HttpError as e:
        print(f"Error with chat system:\n{e}")
        sp(3)
recieved = reading()
label = tk.Label(root,text="loading")
entry = tk.Entry(root)
button = tk.Button(root,text="Send!",command=send)
label.pack()
while True:
    recieved = reading()
    label.config(text=recieved)
    entry.pack()
    button.pack()
    root.update()