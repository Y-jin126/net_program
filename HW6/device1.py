import socket
import random

HOST = 'localhost'
PORT = 7080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Device1 연결됨: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    if data.lower() == 'request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        ilum = random.randint(70, 150)
        response = f"{temp},{humid},{ilum}"
        conn.send(response.encode())
    elif data.lower() == 'quit':
        print("종료 요청 수신. Device1 종료.")
        break

conn.close()
server_socket.close()
