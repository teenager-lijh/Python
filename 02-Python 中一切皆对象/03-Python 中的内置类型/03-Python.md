## 对象的三个特征

1. 身份 对象在内存中的地址，通过函数 `id` 来查看一个对象在内存中的地址，地址就像对象的身份证号
2. 类型：对象是有类型的，比如 `int` `float`  
3. 值：变量是指向实例对象的



## 常见的内置类型

1. `None` ：全局只有一个，在解释器启动的时候，Python 会生成一个 None 对象
2. 数值： `int` `float` `complex` `bool`
3. 迭代类型：可以用 `for` 循环来表里
4. 序列类型：`bytes` `bytearray` `memoryview` `range` `tuple` `str` `array`
5. 映射 `dict`
6. 集合 `set` `frozenset`
7. 上下文管理类型：`with 语句`
8. 其他：`模块类型`、`class和实例`、`函数类型`、`方法类型`、`代码类型`、`object 类型`、`type 类型`、`ellipis 类型，省略号类型`、`notimplemented 类对象`