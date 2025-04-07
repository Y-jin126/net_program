import socket
import time

# 디바이스 서버 주소
DEVICE1_ADDR = ('localhost', 7080)
DEVICE2_ADDR = ('localhost', 7081)

dev1_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dev2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dev1_sock.connect(DEVICE1_ADDR)
dev2_sock.connect(DEVICE2_ADDR)

def save_data(device, values):
    timestamp = time.asctime()
    if device == 1:
        log = f"{timestamp}: Device1: Temp={values[0]}, Humid={values[1]}, Iilum={values[2]}"
    else:
        log = f"{timestamp}: Device2: Heartbeat={values[0]}, Steps={values[1]}, Cal={values[2]}"
    print(">>", log)
    with open("data.txt", "a") as f:
        f.write(log + "\n")

while True:
    cmd = input("> ").strip()

    if cmd == "1":
        dev1_sock.send(b"Request")
        data = dev1_sock.recv(1024).decode()
        values = data.split(",")
        if len(values) == 3:
            save_data(1, values)
        else:
            print("Device1 응답 오류:", data)

    elif cmd == "2":
        dev2_sock.send(b"Request")
        data = dev2_sock.recv(1024).decode()
        values = data.split(",")
        if len(values) == 3:
            save_data(2, values)
        else:
            print("Device2 응답 오류:", data)

    elif cmd.lower() == "quit":
        dev1_sock.send(b"quit")
        dev2_sock.send(b"quit")
        print("모든 디바이스 종료. 프로그램 종료.")
        break

    else:
        print("잘못된 입력입니다. 1, 2 또는 quit 입력")

# 소켓 종료
dev1_sock.close()
dev2_sock.close()
