from socket import *

port = 7080
BUFF_SIZE = 1024

s_sock = socket(AF_INET, SOCK_DGRAM)
print('Listening...')

while True:
    msg = input('Enter a message("send mboxId message" or "receive mboxId"): ')
    if msg == 'quit':
        break
    s_sock.sendto(msg.encode(), ('localhost', port))
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    print(data.decode())
s_sock.close()
