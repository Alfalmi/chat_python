import socket 
import thrending
import queue

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind('localhost', 9999)


def recieve():
    while True:
        try:
            messages. ad = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass


def broadcast():
    while True:
        while not messages.empty():
            message, addr = messages.get()
            print(message, addr)
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message, decode().index(':') + 1:]
                        server.sendto(f"{name} joined:", client)

                    else:
                        server.sendto(message)

                except:clients.remove(client)

t1 = threading.Thread(target=recieve)
t2 = threading.Thread(target=broadcast)
t1.start()
t2.start()