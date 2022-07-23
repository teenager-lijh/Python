#1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

#通过非阻塞io实现http请求
# select + 回调 + 事件循环
#  并发性高
# 使用单线程

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()
#使用select完成http请求
urls = []
stop = False


class Fetcher:
    """
    使用类来完成是因为
    当 把回调函数写在 类的内部的时候
    可以接收到类的实例对象 self
    否则是拿不到 self 的成员变量的
    """
    def connected(self, key):
        """
        当回调 connected 函数的时候
        就说明 socket 就已经是连接状态了
        此时就不需要不停地 循环检测了
        """
        # 在 selector 中注销掉当前的 socket
        selector.unregister(key.fd)
        # 发送 http 请求
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        """
        当发送 http 请求后
        这时候需要等待服务器返回数据
        就需要监听当前数据是否已经发送回来 ==> 即 是否可读

        当它变为可读的状态的时候，不代表可以一直从内核空间读取数据
        所以这时候就可能会抛出异常
        """
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 当 d 为空的时候，说明数据已经读完了
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册
        # 1. self.client.fileno() ==> socket 的文件描述符
        # 2. EVENT_WRITE ==> 写事件 ==> 当自己定义的 socket 对象可以写的时候
        #    也就是 已经连接到了别人家的服务器时，自己想 socket 中写数据然后发送给服务器
        # 3.
        print('file number : ', self.client.fileno(), type(self.client.fileno()))
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    #事件循环，不停的请求socket的状态并调用对应的回调函数
    #1. select本身是不支持register模式
    #2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            # ready 是就绪的意思 ==> 代表已经就绪的 那些注册进去的文件们
            # 这里的 key.data 是在注册的时候写传入的回调函数
            # key.fd 是注册时候的 self.client.fileno() 的返回值
            call_back = key.data
            call_back(key)
    #回调+事件循环+select(poll\epoll)

if __name__ == "__main__":
    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time()-start_time)

# def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
# 
#     #建立socket连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect((host, 80)) #阻塞不会消耗cpu
#     except BlockingIOError as e:
#         pass
# 
#     #不停的询问连接是否建立好， 需要while循环不停的去检查状态
#     #做计算任务或者再次发起其他的连接请求
# 
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#             break
#         except OSError as e:
#             pass
# 
# 
#     data = b""
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError as e:
#             continue
#         if d:
#             data += d
#         else:
#             break
# 
#     data = data.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#     client.close()




