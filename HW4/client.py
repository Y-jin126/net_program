from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9000))
while True:
    msg = input('Input(+, -, *, /):')
    if msg == 'q':
        break
    s.send(msg.encode())
    print('Received message:', s.recv(1024).decode())
s.close()