"""
C10M 问题
如何利用 8 核 CPU 64G内存 在 10gbps 的网络上保持 1000 万的并发连接

    1. 回调模式编码复杂度高
    2. 同步编程的并发性不高
    3. 多线程编程需要线程同步 通过 lock 锁来完成

解决方法：
    1.采用同步的方式来完成异步的代码
    2.用单线程切换任务　用户级别的任务切换，需要用户来实现任务调度
    3.好处是，不需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换
    
完成函数之间的切换：
    1. 需要一个可以暂停的函数，因为函数的运行需要维护一个栈
    2. 并且在适当的时候恢复该函数的继续执行
    ==> 为了解决这个问题就出现了 协程 ==> 可以暂停的函数(可以在暂停的地方传入值) ==> 有多个入口的函数
    ==> 传统的函数是要调用栈的，现在不是栈了 ==> 生成器就是一个可以暂停的函数
"""