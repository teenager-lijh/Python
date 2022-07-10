## Python 魔法函数总览

非数学运算

字符串表示:  `__repr__` `__str__`

集合、序列相关:  `__len__` `__getitem__` `__setitem__` `__delitem__` `__contains__`

迭代相关 `__iter__` `__next__`

可调用 `__call__`

with上下文管理器 `__enter__` `__exit__`

数值转换:  `__abs__` `__bool__` `__int__` `__float__` `__hash__` `__index__`

元类相关:  `__new__` `__init__`

属性相关:  `__getattr__`  `__setattr__` `__getattribute__` `__setattribute__` `__dir__`

属性描述符:  `__get__` `__set__`  `__delete__`

协程:  `__await__` `__aiter__` `__anext__` `__aenter__` `__aexit__`



数学运算

一元运算符: `__neg__（-）` `__pos__（+）` `__abs__`

二元运算符: `__lt__(<)`  `__le__ <=`   `__eq__ ==`   `__ne__ !=`   `__gt__ >`   `__ge__ >=`


算术运算符:  `__add__ +`   `__sub__ -`   `__mul__ *`   `__truediv__ /`   `__floordiv__ //`   `__mod__ %`   `__divmod__ divmod()`   `__pow__ ** 或 pow()`   `__round__ round()`

反向算术运算符: `__radd__`   `__rsub__`   `__rmul__`   `__rtruediv__`   `__rfloordiv__`   `__rmod__`  `__rdivmod__`   `__rpow__`

增量赋值算术运算符:`__iadd__`   `__isub__`   `__imul__`   `__itruediv__`   `__ifloordiv__`   `__imod__`  `__ipow__`

位运算符: `__invert__ ~`   `__lshift__ <<`   `__rshift__ >>`   `__and__ &`   `__or__ |`   `__xor__ ^`

反向位运算符: `__rlshift__`   `__rrshift__`   `__rand__`   `__rxor__`   `__ror__`

增量赋值位运算符: `__ilshift__`   `__irshift__`   `__iand__`   `__ixor__`   `__ior__`



实现 `__call__` 方法，那么当前实例对象就是可调用的，类对象实现 `__init__` 方法，那么类对象就可以调用