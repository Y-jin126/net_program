import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(2)
while True:
    client, addr = sock.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    name = client.recv(1024).decode()
    print(name)
    num = '20221325'
    client.send(num.encode())
    print(num.decode())
    client.close()