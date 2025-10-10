import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  
port = 65432

server_socket.bind((host, port))

server_socket.listen(1)
print(f"Server berjalan di {host}:{port}")
print("Menunggu koneksi dari client...")

conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

while True:

    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Pesan dari client: {data}")

    balasan = f"Pesan '{data}' diterima oleh server."
    conn.send(balasan.encode())

conn.close()
print("Koneksi ditutup.")
