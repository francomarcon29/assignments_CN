import socket

import threading


stop_loop = False


def handshake():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('143.47.184.219', 5378))
        global stop_loop
        if stop_loop:
            break
        try:
            message = input('') + '\n'
            client.sendall(message.encode('utf-8'))
            msg = client.recv(2048).decode('utf-8')
            if msg == 'IN-USE':
                client.close()
                stop_loop = True
                continue
            else:
                print(msg)
                break

        except OSError as msg:
            print(msg)
            client.close()
            break
    return client


def write(client_saved):
    while True:
        global stop_loop
        if stop_loop:
            #print(stop_thread)
            break
        try:
            message = input('') + '\n'
            if message == '!quit\n':
                client_saved.close()
                break
                #stop_thread = True
            elif message == '!who\n':
                msg = 'WHO' + '\n'
                client_saved.send(msg.encode('utf-8'))
            elif message.startswith('@'):
                client_saved.send(f'SEND {message}'.encode('utf-8'))
            else:
                #print(message)
                client_saved.send(message.encode('utf-8'))

        except OSError as msg:
            client_saved.close()
            break


def receive(client_saved):
    while True:
        try:
            message = client_saved.recv(2048).decode('utf-8')
            print(message)
            
        except OSError as msg:
            print(msg)
            client_saved.close()
            break




client_saved = handshake()

receive_thread = threading.Thread(target=receive, args= [client_saved])
receive_thread.start()

write(client_saved)



#socket close
#buffer dinamico
#one thread for receive

