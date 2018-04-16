# Author: BigRabbit
#  上午10:25

# ***************************************
# itertools模块提供了许多与迭代器相关的函数，
# 为我们提供了很多便利
# ***************************************


import itertools


# 1、islice()

# ***************************************
# 迭代器切片
# 我们经常会对字符串、列表进行切片操作，
# 但是我们却不能使用通常的切片方式对迭代器进行操作，
# 我们需要用到itertools中的islice()。
# ***************************************

# 对列表与字符串进行切片操作

list1 = [1, 2, 3, 4]
print(list1[0:3])             # [1, 2, 3]


str1 = 'abcd'
print(str1[0:3])              # abc


# 那么，我们对一个迭代器使用我们通常的切片操作会怎样呢？

generator1 = (i for i in range(10))
# print(generator1[0:5])

# TypeError: 'generator' object is not subscriptable


# 由此看来，我们对列表、字符串可以使用的标准切片操作，
# 到了迭代器这里行不通了，那么使用itertools中的islice()呢？

print([i for i in itertools.islice(generator1, 0, 8, 2)])

# [0, 2, 4, 6]


def generator2(n):

    while True:
        yield n
        n += 1


# print(generator2(0)[0:10])

# TypeError: 'generator' object is not subscriptable


print([i for i in itertools.islice(generator2(0), 0, 10)])

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先
# 我们并不知道 (并且也没有实现索引)。
# 函数 islice() 返回一个可以生成指定元素的迭代器，
# 它通过遍历并丢弃直到切片开始索引位置的所有元素。
# 然后才开始一个个的返回元素，并直到切片结束索引位置。

# 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。
# 必须考虑到迭代器是不可逆的这个事实。所以如果你需要之后再次访问
# 这个迭代器的话，那你就得先将它里面的数据放入一个列表中。

# ---------------------------------------------


# 2、dropwhile()

# *********************************************
# 跳过一个可迭代对象特定的开头部分
# 有时候，我们不需要可迭代对象的所有内容，只需要某些行之后的内容，
# 比如说，有一个.py文件，该文件的开头部分是关于该文件的功能的介
# 绍的注释部分，而我们需要该文件的正文，那么我们要怎么做呢？

# 下面有两种方法，一种使用了itertools中的dropwhile()函数，而
# 另一种则没有使用itertools中的dropwhile()函数，对比一下。
# **********************************************

# 首先是不使用itertools.dropwhile()函数的方法

with open('test4.py', 'r') as f:

    # 得到第一行不以'#'开头的内容
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # 得到我们需要的正文内容
    while line:
        print(line)
        line = next(f, None)

# 上面的代码实现了我们的需求，test4.py中除去开头注释部分的其他内容
# 第一个while循环用来判断读取到的内容是否以'#'开头，直到读取到的内
# 容不再以'#'开头，跳出第一个while循环，进入第二个while循环中。


# 接下来，是使用itertools.dropwhile()函数的方法


with open('test4.py', 'r') as f:

    for line in itertools.dropwhile(
            lambda context: context.startswith('#'), f
    ):
        print(line)

# 匿名函数中的context就是我们从test4.py中读取的每行内容，当它以'#'
# 开头时，dropwhile函数就会把该行内容删除掉，继续读取下一行内容，直
# 到它不再以'#'开头，那么从该行内容到文件结尾的所有内容都会返回给我们


# 对比上面两种方法，第二种方法是不是简化了很多，不过值得注意的是，有人可
# 能会对第一种方法做如下的修改

with open('test4.py', 'r') as f:
    for line in (
            context for context in f if not context.startswith('＃')
    ):
        print(line)

# 这种方法与第一种方法相比，简化了不少，但是，你应该发现除了开头的注释部分
# 会被过滤掉外，文中的其他以'#'开头的内容也会被过滤掉，和我们的要求不符合

# ---------------------------------------------


# 3、permutations()\combinations()\
# combinations_with_replacement()

# **********************************************
# 如果你想迭代一个集合中元素所有的排列组合情况，
# itertools提供了三个与排列组合相关的函数
# **********************************************

list2 = [1, 2, 3, 4]

# permutations()

# 该函数接收一个可迭代对象，返回一个permutations对象
# 迭代遍历结果为元组，包含元素的所有排列情况
# 该排列的结果是会考虑元素的顺序的

for item in itertools.permutations(list2):
    print(item)

# 结果为 4*3*2*1,总共是24个结果

# (1, 2, 3, 4)
# (1, 2, 4, 3)
# (1, 3, 2, 4)
# (1, 3, 4, 2)
# (1, 4, 2, 3)
# (1, 4, 3, 2)
# (2, 1, 3, 4)
# (2, 1, 4, 3)
# (2, 3, 1, 4)
# (2, 3, 4, 1)
# (2, 4, 1, 3)
# (2, 4, 3, 1)
# (3, 1, 2, 4)
# (3, 1, 4, 2)
# (3, 2, 1, 4)
# (3, 2, 4, 1)
# (3, 4, 1, 2)
# (3, 4, 2, 1)
# (4, 1, 2, 3)
# (4, 1, 3, 2)
# (4, 2, 1, 3)
# (4, 2, 3, 1)
# (4, 3, 1, 2)
# (4, 3, 2, 1)

# 我们也可以指定参加排列组合的元素的个数

for item in itertools.permutations(list2, 2):
    print(item)

# 结果为4*3,总共12个结果

# (1, 2)
# (1, 3)
# (1, 4)
# (2, 1)
# (2, 3)
# (2, 4)
# (3, 1)
# (3, 2)
# (3, 4)
# (4, 1)
# (4, 2)
# (4, 3)

# -------------------------------------------

# combinations()

# combinations()与permutations()的区别在于返回的结果，
# permutations()返回的结果会考虑元素的排列顺序，也就是说
# 在permutations()返回的结果中，(1, 3, 2)与(2, 3, 1)
# 是俩个不同的结果;
# 而combinations()返回的结果是元素的组合情况，不会考虑
# 元素的顺序，所以(1, 2, 3)和(2, 3, 1)被看做同一个结果

for item in itertools.combinations(list2, 3):
    print(item)

# 结果为4*3*2/(1*2*3),总共４个结果

# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)

# ----------------------------------

# combinations_with_replacement()

# 上面的permutations()和combinations()函数都是默认
# 每个元素只可以使用一次，而combinations_with_replacement()
# 函数则可以多次使用同一个元素

for item in itertools.combinations_with_replacement(list2, 3):
    print(item)

# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 1, 4)
# (1, 2, 2)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 3)
# (1, 3, 4)
# (1, 4, 4)
# (2, 2, 2)
# (2, 2, 3)
# (2, 2, 4)
# (2, 3, 3)
# (2, 3, 4)
# (2, 4, 4)
# (3, 3, 3)
# (3, 3, 4)
# (3, 4, 4)
# (4, 4, 4)

# ***********************************
# 这三个与排列组合相关的函数为我们提供了很大的便利，
# 在恰当的时候使用他们，能节省我们大量的时间
# ***********************************

# -----------------------------------


# 4、zip_longest()

# 要说itertools中的zip_longest(),那么我们需要先说说
# zip()函数

# zip()

# zip()函数可以将多个可迭代对象的同一位置的元素组合为一个
# 元组，最终返回的是一个迭代器 - zip object
# (值得注意的是，在python2中，返回的是一个列表；
# 在python3中，对zip()做了优化，返回一个迭代器)

# 举个关于zip()函数的例子

list3 = [1, 2, 3, 4]
tuple1 = ('a', 'b', 'c', 'd')

for item in zip(list3, tuple1):
    print(item)

# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')

# 上面的例子中，list3和tuple1中的元素个数是相等的，
# 如果他们的元素个数不相等呢？请看下面的例子

tuple2 = ('q', 'w', 'e')

for item in zip(list3, tuple2):
    print(item)

# (1, 'q')
# (2, 'w')
# (3, 'e')

# 你会发现，结果只有３个，所以zip()的最终结果以最短的为准，
# 就像我们熟知的木桶理论一样
# 但是如果我们想让结果以最长的为准呢？itertools中的zip_longest()
# 就派上用场了，看下面的例子

for item in itertools.zip_longest(list3, tuple2):
    print(item)

# (1, 'q')
# (2, 'w')
# (3, 'e')
# (4, None)

# 这次的结果是4个，以最长的为准，缺少的元素会被标记为None

# 当你想成对的处理数据时，你应该考虑一下zip()或者zip_longest()

# -----------------------------------


# 5、chain()

# ***********************************
# 如果你有多个可迭代对象，你将要对他们进行同样的操作，你会不会
# 对他们分别进行迭代然后进行你需要的操作？即使他们都是同一类型
# 的，你可以对他们进行拼接后进行迭代与你需要的操作。这些都很费
# 你的时间与机器资源，那么这时候你应该尝试一下itertools中的
# chain()函数，说不准会有意想不到的效果。看下面的例子
# ************************************

list4 = [1, 4, 15, 9, 20]
tuple3 = (2, 13, 3, 5)

result = [
    item**2 for item in itertools.chain(list4, tuple3)
    if item < 5
]
print(result)  # [1, 16, 4, 9]

# 我们知道list与tuple不能直接进行拼接，只能分别迭代；而使
# 用itertools中的chain()可以帮助我们完成一些不必要的操作
