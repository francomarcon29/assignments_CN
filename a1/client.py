import socket

import threading



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('143.47.184.219', 5378))

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if 'IN-USE' in message:
                print(message)
                client.close()
            else:
                print(message)
            
        except:
            print('An error occurred!')
            client.close()
            break

def write():
    while True:
        message = input('') + '\n'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

'''write_thread = threading.Thread(target=write)
write_thread.start()'''

write()

#socket close
#buffer dinamico
