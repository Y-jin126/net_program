import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
name = 'Yejin Kwon'
sock.send(name.encode())
id = sock.recv(1024)
print(id.decode())
sock.close()