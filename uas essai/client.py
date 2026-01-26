import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"   # IP server
port = 12345

client_socket.connect((host, port))

message = "Halo server, ini pesan dari client"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("Balasan dari server:", response)

client_socket.close()
