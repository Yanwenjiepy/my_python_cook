# Author: BigRabbit
# 上午11:12

# &&&&&&&&&& Python中的推导式 &&&&&&&&&&

# 列表、字典、集合推导式很有用，很简洁，很Pythonic，
# 在适当的时候使用这些推导式能够提高程序的性能，减少资源的占用

# ----------------------------------------------------------


# &&& 列表推导式 &&&

# ------------------------------------


# && 只有 if 条件语句，通常用来过滤数据 &&

# list1 = [表达式 for i in range(5) if 1 < i < 4]
# list1： 推导式生成的新列表
# 表达式： 1、关于i的一个表达式 2、接收i作为参数并且有返回值的函数
# if 1 < i < 4： 通过条件对 i 进行过滤

# 直接在列表推导式内写简单的表达式

list1 = [i**2 for i in range(5) if i % 2 == 0]
# print(list1)                                      # [0, 4, 16]


# 表达式为函数

def test_sum(j):
    result = j + 2
    return result


list2 = [test_sum(i) for i in range(5) if i % 2 == 0]
# print(list2)                                      # [2, 4, 6]

# ---------------------------------------


# && 包含'if -- else --'语句，通常用来对输出的数据进行统一

"""
比如 有一个包含有str类型的数字'1','2'和int类型的3,4的列表

test_list = ['1', '2', 3, 4],

我们希望这个列表中的所有元素都是int类型的，
就可以使用包含'if--else--'语句的列表推导式来实现。

new_list = [i if type(i) is int else int(i) for i in test_list]
结果为[1, 2, 3, 4]

"""

# list3 = [表达式1 if i == 1 else 表达式2 for i in range(5)]
# 表达式1：当i满足'if i == 1'条件时执行
# 表达式2：不满足'if i == 1'条件的i将会执行表达式2

list3 = [i*2 if i == 1 else i**2 for i in range(5)]
# print(list3)                                      # [0, 2, 4, 9, 16]

# ------------------------------------------------------------


"""
    生成器是Python中很厉害的一个特性，以后要在合适的地方多多使用。
    生成器包括生成器函数和生成器表达式两种类型。
    生成器函数就是将普通函数的'return'替换为'yield'的函数；
    生成器表达式与列表生成式很类似，下面的代码就是生成器表达式。
"""

# &&& 生成器表达式 &&&

# 只需要把列表推导式的'[]' 换成'()' ，那么这就是一个生成器表达式

from collections import Iterable
from inspect import isgenerator
import types

generator1 = (test_sum(i) for i in range(5) if i % 2 == 0)
print(type(generator1))                              # <class 'generator'>

print(isinstance(generator1, types.GeneratorType))   # True
# 可以使用上面的方法来判断generator1是否是生成器类型

print(isgenerator(generator1))                       # True
# 判断是否是生成器
# isgengerator()函数其实返回了上面使用isinstance()的操作

print(isinstance(generator1, Iterable))              # True
# 判断generator1是否可以迭代
# 生成器是迭代器的一种

list4 = [j for j in generator1 if j % 2 == 0]
print(list4)                                         # [2, 4, 6]

# ---------------------------------------------------------------


# &&& 字典推导式 &&&
dict1 = {k: k*2 for k in generator1 if k % 2 == 0}
print(dict1)                                         # {2: 4, 4: 8, 6: 12}

# ----------------------------------------------------------------


# &&& 集合推导式 &&&
list5 = [m if m % 2 == 0 else m*2 for m in range(5)]
print(list5)                                         # [0, 2, 2, 4, 6]

set1 = {n for n in list5}
print(set1)                                          # {0, 2, 4 ,6}

# -----------------------------------------------------------------


# &&&&& 总结 &&&&&

# 1、Python中的推导式 简洁、高效、Pythonic,在合适的地方就尽情的使用吧

# 2、列表推导式有两种常见的形式：
#       只包含'if--'条件语句的，通常用来过滤数据；
#       包含'if--else--'语句的，通常用来让结果保持统一

# 3、字典推导式在实现有一定规律的字典时，很好用

# 4、集合推导式通常可以用在对序列、可迭代对象的去重情况中

# 5、生成器是Python中很有用的一个特性，包括生成器表达式和生成器函数
#    本次主要是简单介绍了一下生成器表达式，以后将写一个介绍生成器的总结
#    所有的生成器都是迭代器，可以使用'for--in--'来进行迭代，
#    值得注意的是，生成器由于在需要值的时候才会去生成相应的值，大大节省了资源
#    所以在能够使用生成器的地方就不要使用其他的方式去实现
