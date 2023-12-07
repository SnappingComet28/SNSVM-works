import dropbox as dbx
db = dbx.Dropbox("sl.BqBZszXdRrDTOcUaC8duoMxf2uvDx0qzoZMGqARfhNRUbbPrKPOs_sY2IIaKP4pTwyLJaOuwZIBwq4_LqeU5aTN9BZNZJqNN4UOJzHR8r3eEeoAkD0uXR")

db.files_upload("helo".encode('utf-8'),"/test/ppl2.txt")
print("done")