"""
IPV4 UDP 协议

下方的注释引用到这里的 IP_server:PORT_server
IP_server = 本机IP :PORT_server = 6666
代码中的 0.0.0.0 并不是本机 IP 这个并不是要填到 UDP 报文中的
"""
import socket
import threading
# 这个 socket 只是用来监听的
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8004))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print("get message : ", data)
        re_data = input('input message : ')
        if re_data == 'end':
            break
        sock.send(re_data.encode('utf8'))

    server.close()
    sock.close()


while True:
    # 这里的 sock 才是用来通信的
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()



