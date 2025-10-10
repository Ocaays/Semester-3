import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 65432

client_socket.connect((host, port))
print(f"Terhubung ke server {host}:{port}")

while True:

    pesan = input("Ketik pesan ke server ('exit' untuk keluar): ")
    if pesan.lower() == 'exit':
        break
    client_socket.send(pesan.encode())

    data = client_socket.recv(1024).decode()
    print(f"Balasan dari server: {data}")

client_socket.close()
print("Koneksi ke server ditutup.")
