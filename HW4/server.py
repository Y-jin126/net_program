from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(5)
print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            num1, cal, num2 = data.decode().split()
            num1 = int(num1)
            num2 = int(num2)
            if cal == '+':
                rsp = num1 + num2
            elif cal == '-':
                rsp = num1 - num2
            elif cal == '*':
                rsp = num1 * num2
            elif cal == '/':
                rsp = num1 / num2
                rsp = round(rsp, 1)
        except:
            client.send(b'Try again')
        else:
            client.send(str(rsp).encode())
    client.close()
