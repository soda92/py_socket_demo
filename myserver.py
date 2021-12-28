import socket
import sys, threading


class ServerThread(threading.Thread):
    def __init__(self, host, port, callback):
        threading.Thread.__init__(self)
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (host, port)
        print("starting up on %s port %s" % server_address, file=sys.stderr)
        self.sock.bind(server_address)

        # Listen for incoming connections
        self.sock.listen(1)
        self.callback = callback
        self.connection, self.client_address = self.sock.accept()
        # self.connection.settimeout(0.1)
        while True:
            try:
                data = self.connection.recv(16)
                if data:
                    self.callback(data.decode())
                    if data.decode() == "exit":
                        break
            except TimeoutError:
                continue


if __name__ == "__main__":
    port = 8001
    address = "localhost"
    thread = ServerThread(address, port, print)
    thread.start()
