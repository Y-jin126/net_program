from socket import *

BUFF_SIZE = 1024
port = 7080

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

mybox = {}
sendmsg = ''


while True:
    msg, addr = s_sock.recvfrom(BUFF_SIZE)
    try:
        opt, mboxID, message = msg.decode().split(' ', 2)
    except ValueError:
        opt, mboxID = msg.decode().split(' ', 1)
    if opt == 'send':
        if mboxID not in mybox:
            mybox[mboxID] = [message]
        else:
            mybox[mboxID].append(message)
        
        sendmsg = "OK"
    
    elif opt == 'receive':
        if mboxID not in mybox:
            sendmsg = "No messages"
        else:
            if mybox[mboxID]:
                sendmsg = mybox[mboxID][0]
                mybox[mboxID].pop(0)
            else:
                sendmsg = "No messages"
    
    s_sock.sendto(sendmsg.encode(), addr)
