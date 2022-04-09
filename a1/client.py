import socket

PORT = 5050
SERVER = "145.108.73.134"
ADDR = (SERVER, PORT)

DISCONNECT_MESSAGE = "!DISCONNECT"





client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (2048 - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello")
input()
send(DISCONNECT_MESSAGE)
input()