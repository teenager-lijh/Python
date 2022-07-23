import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8004))

while True:
    re_data = input('input message : ')
    if re_data == 'end':
        break
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print("get message : ", data)

client.close()
