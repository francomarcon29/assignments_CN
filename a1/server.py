#Import the socket library

import socket

#Import threading

import threading


#Specifying PORT and Server IP

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


#Variables

DISCONNECT_MESSAGE = "!DISCONNECT"


#Make a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client(conn, addr):
    print(f"New Connection: {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(2048).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"HELLO-FROM {addr}")

    conn.close()



def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections = {threading.activeCount() -1}")

print("Server is starting...")

start()
