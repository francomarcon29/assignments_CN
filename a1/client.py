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
            if 'IN-USE' in message:
                client.close()
                print(message)
                flag = True
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('143.47.184.219', 5378))
                
                #stop_thread = True      
            else:
                print(message)
            
        except OSError as msg:
            print(msg)
            client.close()
            break

def write():
    while True:
        global stop_thread
        if stop_thread:
            #print(stop_thread)
            break
        try:
            message = input('') + '\n'
            if message == '!quit\n':
                client.close()
                break
                #stop_thread = True
            elif message == '!who\n':
                msg = 'WHO' + '\n'
                client.send(msg.encode('utf-8'))
            elif message.startswith('@'):
                client.send(f'SEND {message}'.encode('utf-8'))
            else:
                #print(message)
                client.send(message.encode('utf-8'))

        except OSError as msg:
            client.close()
            break



receive_thread = threading.Thread(target=receive)
receive_thread.start()

flag = True

write_thread = threading.Thread(target=write)
write_thread.start()


#socket close
#buffer dinamico
