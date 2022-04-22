import socket

import threading




def handshake():
    stop_loop = False
    while stop_loop == False:
        print("Insert name: ")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('143.47.184.219', 5378))
        message = "HELLO-FROM "
        nameUser = input()
        message = message + nameUser + '\n'
        client.sendall(message.encode('utf-8'))
        msg = client.recv(2048).decode('utf-8')
        if msg == "HELLO " + nameUser + "\n":
            print("Username accepted")
            stop_loop = True
        if msg == 'IN-USE':
            client.close()
            stop_loop = False
            continue
    return client


def write(client_saved):

    while True:
        try:
            message = input('') + '\n'
            if message == '!quit\n':
                break
                #stop_thread = True
            elif message == '!who\n':
                msg = 'WHO' + '\n'
                client_saved.sendall(msg.encode('utf-8'))
            elif message.startswith('@'):
                client_saved.sendall(f'SEND {message[1:]}'.encode('utf-8'))
            else:
                #print(message)
                client_saved.send(message.encode('utf-8'))

        except OSError as msg:
            print(msg)
            client_saved.close()
            break


def receive(client_saved):
    message = ""
    while True:
        try:
            temp = client_saved.recv(1).decode('utf-8')
            message = message + temp
            if message.endswith("\n"):
                if message.startswith("WHO-OK"):
                    print('Connected users: ')
                    print([message[5:]])
                elif message.startswith("UNKNOWN"):
                    print('This user does not exit')
                elif message.startswith('SEND-OK'):
                    print(message)
                #elif message.startswith('DELIVERY'):
                #    print(message[8:])

            
        except OSError as msg:
            print(msg)
            client_saved.close()
            break




client_saved = handshake()

receive_thread = threading.Thread(target=receive, args= [client_saved], daemon=True)
receive_thread.start()

write(client_saved)



#socket close
#buffer dinamico
#one thread for receive