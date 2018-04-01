# Author: BigRabbit
# 上午10:47

# -------------------------------

# 生成器是一类特殊的迭代器，生成器在Python中用处很多，
# 在适当的地方使用生成器能带来很多好处
# 因为生成器的用处较多，我单独写了一个关于生成器用法的文件，
# 这个文件只包括迭代器的相关用法

# --------------------------------

#     迭代是Python强大的功能之一

# 与生成器相比，迭代器是比较底层的特性，
# 虽然平时并没有生成器的出场率高，但是它很重要，
# 是生成器的基础

# 迭代器是一个实现了迭代器协议的容器对象

# 首先明确几个概念

# 可迭代对象：实现了__iter__()方法的对象
# 迭代器：实现了__next__()方法的对象

# 通过调用__iter__()方法，可迭代对象返回一个迭代器，
# 通过调用__next__()方法，进行迭代操作

# 几乎所有的容器对象以及文件对象、管道对象等都是可迭代对象

# ----------------------------------

# **********************************
# 通常情况下，我们会使用for循环语句来遍历一个可迭代对象，
# 但如果你需要对迭代进行更精确的控制，那么我们可以手动使用
# next()函数进行遍历，自己捕获StopIteration异常
# **********************************

# 使用for循环读取文件
with open('./test.txt') as f:
    for line in f:
        print(line, end='')


# 使用next()函数并且捕获StopIteration,来手动读取文件
with open('./test.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


# 通过使用None来代替StopIteration,标记迭代结束
with open('./test.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

# --------------------------------


# ********************************
# 自定义迭代器

# 我们需要实现__next__与__iter__方法

# 下面的例子中，__student_list是一个列表，
# 列表实现了__next__与__iter__方法
# 我们自己实现了__iter__方法，返回了列表的迭代器
# ********************************

class MyIteration(object):

    __student_list = []

    def add_student(self, student):
        if isinstance(student, str):
            self.__student_list.append(student)

    def __iter__(self):
        return iter(self.__student_list)


test = MyIteration()
test.add_student('小明')
test.add_student('小红')
for student in test:
    print(student)

# --------------------------------


# ********************************
# 按顺序迭代多个排序可迭代对象的合并序列

# 有多个经过排序的可迭代对象，
# 我们想要将他们合并为一个可迭代对象，
# 然后对合并后的序列进行顺序迭代

# 我们可以使用heapq.merge()函数来实现
# *********************************

import heapq

result = heapq.merge([1, 4, 7, 9], [17, 23], [32], [8, 12, 15, 99])

# 注意结果是一个生成器，所以我们用来合并多个很长的序列，然后迭代合并后的序列
print(result)  # <generator object merge at 0x7fe32c37eb48>

print([i for i in result])  # [1, 4, 7, 8, 9, 12, 15, 17, 23, 32, 99]


# 我们可以用heapq.merge()函数来合并多个文件
# file1、file2、file3都是经过排序的文件
# 我们将这三个文件的内容合并且排序后写入file4

with open('file1') as f1, \
        open('file2') as f2, \
        open('file3') as f3, \
        open('file4', 'wt') as f4:

    for context in heapq.merge(f1, f2, f3):
        f4.write(context)


# 有一点要强调的是 heapq.merge() 需要所有输入序列必须是排过序的。

# 它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。

# 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有
# 输入序列中的元素都被遍历完。

# --------------------------------


# ********************************
# 使用迭代器来代替while循环

# 我们在socket网络编程中，经常需要通过socket发送、读取数据
# 我们通常是在while循环中不断执行send()和recv()，
# 并且添加终止条件来判断是否发送或者接收完毕。
#
# 而使用iter()可以简化很多，
# 使用一个简单的 iter() 调用就可以将两者结合起来了
# *********************************


# 这是一个负责读取socket中数据并写入到文件中的函数

def reader1(my_socket):
    while True:
        data = my_socket.recv(1024)
        if data == b'':
            break
        with open('./test.txt', 'wb') as f:
            f.write(data)


def reader2(my_socket):
    for data in iter(lambda: my_socket.recv(1024), b''):
        with open('./text.txt', 'wb') as f:
            f.write(data)

# 对比发现，代码简化了一些，

# iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和
# 一个标记 (结尾) 值作为输入参数。当以这种方式使用的时候，它会创建
# 一个迭代器，这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止。
