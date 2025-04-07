import socket
import random

HOST = 'localhost'
PORT = 7081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Device2 연결됨: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    if data.lower() == 'request':
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        response = f"{heartbeat},{steps},{cal}"
        conn.send(response.encode())
    elif data.lower() == 'quit':
        print("종료 요청 수신. Device2 종료.")
        break

conn.close()
server_socket.close()
