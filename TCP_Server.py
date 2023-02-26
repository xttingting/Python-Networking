import socket
from enum import Enum

# create a server side socket IPV4 and TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostbyname(socket.gethostname()),12345))

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    