import socket
import threading

HOST = '127.0.0.1'  
PORT = 55555

nickname = input("Masukkan nama kamu: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def terima_pesan():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Terputus dari server!")
            client.close()
            break

def kirim_pesan():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

thread_receive = threading.Thread(target=terima_pesan)
thread_receive.start()

thread_send = threading.Thread(target=kirim_pesan)
thread_send.start()
