## 并发 并行

并发：一个时间段内，有多个程序在同一个 cpu 上运行，但是任意时刻只有一个程序在 cpu 上运行

并行：任意时刻点上，有多个程序运行在多个 cpu 上



## 同步 异步

消息通信的一种机制：

同步：同步是指代码调用 IO 操作时，必须等待 IO 操作完成才能返回的调用方式

异步：异步是指代码调用 IO 操作时，不必等待 IO 操作完成就返回的调用方式



## 阻塞 非阻塞

是函数调用的一种机制：

阻塞：阻塞是指调用函数时，当前线程被挂起

非阻塞：非阻塞是指调用函数时，当前线程不会被挂起，而是立即返回