import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('143.47.184.219', 5378))

done = False

while not done:
    msg_send = input() + '\n'
    client.send(msg_send.encode('utf-8'))
    msg = client.recv(2048).decode('utf-8')
    if msg_send == '!quit\n':
        done = True
    elif msg_send == '!who\n':
        client.send('WHO\n'.encode('utf-8'))
    elif msg_send.startswith('@'):
        pass
    else:
        print(msg)


client.close() 

