import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = '127.0.0.1', 9001
server.bind((host, port))
server.listen(10)
user_connected = True
socket_object = [server]

print("Welcome to the J.M.R Server")

while user_connected:
    socket_list_read,socket_list_write,socket_list_error = select.select(socket_object, [], socket_object)