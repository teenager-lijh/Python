## 五层网络模型

![image-20220713202212937](01-Python.assets/image-20220713202212937.png)



`Socket` 是一个 `API`，通过这个接口可以直接和 `传输层` 打交道

`Socket` 理解为插座，把 `数据` 理解为电力，只要把数据插在插座上，就可以完成数据的传输了，而传输层以及它下边的网络层都抽象为了电力传输系统

传输层的 `TCP` 和 `UDP` 协议传输数据是双向的，双方都可以随时向对方发送数据