import time
import socket
from sklearn import datasets

data = datasets.load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected!\n".encode())
    client.send(f"{data['data'][:,0]}".encode())
    time.sleep(2)
    client.send("you are being disconnected\n".encode())