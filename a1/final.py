import socket

import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('143.47.184.219', 5378))


stop_thread = False



def receive():
    while True:
        global stop_thread
        if stop_thread:
            #print(stop_thread)
            break
        try:
            message = client.recv(2048).decode('utf-8')
            print(message)
            
        except OSError as msg:
            print(msg)
            client.close()
            break



def write():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('143.47.184.219', 5378))
        global stop_thread
        if stop_thread:
            #print(stop_thread)
            break
        try:
            message = input('') + '\n'
            client.sendall(message.encode('utf-8'))
            msg = client.recv(2048).decode('utf-8')
            if msg == 'IN-USE':
                client.close()
                stop_thread = True
            else:
                receive()

        except OSError as msg:
            client.close()
            break



receive_thread = threading.Thread(target=receive)
receive_thread.start()


write()

#socket close
#buffer dinamico

#one thread for receive

