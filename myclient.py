import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("localhost", 8001))
# s.sendall("string".encode())
s.connect(("localhost", 8001))
s.settimeout(.1)
while True:
    string = input()
    s.sendall(string.encode())

    if string == "exit":
        break
