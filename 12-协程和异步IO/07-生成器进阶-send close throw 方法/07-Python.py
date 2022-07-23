"""
生成器进阶 send close throw

希望：
    1. 生成器不仅能传出值, 还能传进来值
"""

def gen_func():
    # 1. 可以产出值
    # 2. 可以传递值到生成器内部
    html = yield 'http://projectsedu.com'
    print(html)
    yield 2
    yield 3
    return 'lijh'

# 生成器可以暂停
# 启动生成器的两种方式 next() 或者 调用生成器对象的 send

generator = gen_func()

"""
send 方法不仅可以传递值到生成器内部
还可以重启生成器到下一个 yield 的位置

在第一次使用 send 方法启动生成器的时候
只能传递一个 None 值进去

先产出一个值，再接收一个值
html = yield 'http://projectsedu.com' 这行代码分两步
1. 产出值
2. 接收值

使用 send 方法的时候必须是即将要执行接收值的那一步才行
而在生成器 一次都没有启动过的时候是不能够直接执行第 2 步接收值的步骤的
"""

generator.send(None)
print(next(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))