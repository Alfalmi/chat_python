import socket
import thrending
import random

client = socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Enter your name: ")

def recieve():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=recieve)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), ('localhost', 9999))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ('localhost', 9999))