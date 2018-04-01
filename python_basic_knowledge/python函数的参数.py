# Author: BigRabbit
#  下午6:47

'''
    ******函数中的参数*******

    Python中函数的参数包括 位置参数、默认参数，可变参数、关键字参数，

    这也定义函数时候，函数参数的书写与传入顺序

'''

# 位置参数与默认参数
# 位置参数必须按顺序传入值；
# 如果默认参数不传入值，则会使用默认值；
# 可变参数与关键字参数可以接收多个值，可变参数返回的是一个tuple,关键字参数返回的是一个dict
# 通常用 *args 表示可变参数，**kwargs 表示关键字参数


# 如果既包含默认参数，又包含可变参数，则必须先给默认值传值，然后继续给可变参数传值，
# 否则准备传入可变参数的值会传给默认参数，就会出现下面的例1这种情况


def fun_1(name, age=18, *args):
    return name, age, args

# *****例1*****


# print(fun_1('Jack', 'man'))  # ('Jack', 'man', ())
# 'man'这个字符串传给了age这个参数，而age需要的应该是一个int类型的值

print(fun_1('Jack', 18, 'man'))  # ('Jack', 18, ('man',))


print(fun_1('Jack', 20, 30))  # ('Jack', 20, (30,))
# -------------------------------------------------------------


# 当一个函数包含 默认参数 与 可变参数时，默认参数只能进行位置传参，然后对可变参数进行传参
# 因为按照参数的传入顺序，关键字参数应该在最后传入，其他类型参数应该先传入


# 对于默认参数，既可以进行位置传参，也能以关键字形式传参，但不可以同时使用

# print(fun_1('Jack', 20, age=30))
# TypeError: fun_1() got multiple values for argument 'age'

# 当函数没有可变参数和关键字参数但有多个默认参数的时候，可以使用关键字传参，
# 此时调换默认参数的顺序不会影响值的传入，如下

def fun_2(name, age=18, city='Shanghai'):
    return name, age, city


print(fun_2('Jack', city='Beijing', age=20))  # ('Jack', 20, 'Beijing')

# ---------------------------------------------------------------

# 可以使用 *tuple 将一个 tuple 当做可变参数传入


def fun_3(name, age, *args):
    return name, age, args


tuple1 = ('man', 'Shanghai')

print(fun_3('Jack', 20, *tuple1))  # ('Jack', 20, ('man', 'Shanghai'))

# -----------------------------------------------------------------

# 同样，也可以使用 **dict 将一个字典 当做关键字参数传入


def fun_4(name, age, *args, **kwargs):
    return name, age, args, kwargs


tuple2 = ('woman', 'Beijing')
dict1 = {'country': 'Chinese', 'job': 'teacher'}
print(fun_4('Marry', 21, *tuple2, **dict1))
# ('Marry', 21, ('woman', 'Beijing'), {'country': 'Chinese', 'job': 'teacher'})

# ---------------------------------------------------------------
# **********************
# *****命名关键字参数*****
# **********************

'''
    当我们需要对传入的关键字参数进行限制时(限制关键字参数的名字，个数，
    让使用者通过关键字参数的名字就明白要传入什么参数)，我们可以使用命名关键字参数。
'''


# name,age 为位置参数，city 为关键字参数
# 当关键字参数前面没有可变参数时，需要在关键字参数前面添加*，告诉Python解释器 * 后面的参数是关键字参数
def test_1(name, age, *, city):
    return name, age, city


# name, age 为位置参数， *args 为可变参数， city 为关键字参数
# 当命名关键字参数的前面有可变参数时，不需要在命名关键字参数前面添加*
def test_2(name, age, *args, city):
    return name, age, args, city


# 当在调用该函数时，没有使用键值对形式传入city参数时，会报以下错误：

# print(test_2('Jack', 22, 'man', 'teacher'))  # 没有传入city参数
# TypeError: test_1() missing 1 required keyword-only argument: 'city'

# 传入city参数，则正常执行
print(test_2('Jack', 22, 'man', 'teacher', city='beijing'))
# ('Jack', 22, ('man', 'teacher'), 'beijing')

# *****注意*******

# 当函数中的命名关键字参数有默认值时，不传入city参数时会默认使用默认值，是不会报错的


def test_3(name, age, *args, city='Shanghai'):
    return name, age, args, city


print(test_3('Jack', 22, 'man', 'teacher'))
# ('Jack', 22, ('man', 'teacher'), 'Shanghai')

# ----------------------------------------------------------------

# 一般情况下，默认参数和可变参数一同使用的情况很少见；
# 常见的情况为:位置参数与默认参数、位置参数与可变参数、位置参数与可变参数以及关键字参数；
# 通常，在定义函数的参数时候，不要太过于复杂，对于使用和维护，以及以后的重构都会造成不小的麻烦
