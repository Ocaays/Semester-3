import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"   # localhost
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)

print("Server berjalan, menunggu koneksi...")

conn, addr = server_socket.accept()
print("Terhubung dengan client:", addr)

data = conn.recv(1024).decode()
print("Pesan dari client:", data)

response = "Pesan berhasil diterima oleh server"
conn.send(response.encode())

conn.close()
server_socket.close()
