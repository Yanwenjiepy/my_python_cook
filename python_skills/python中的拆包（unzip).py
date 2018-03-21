# Author: BigRabbit
# 17-10-27 上午10:41

"""
                             *** 解 压 ***
    将一个可迭代的对象通过赋值语句进行解压并将其元素赋值给多个变量。
可迭代对象包括：列表list，元组tuple，字符串str，文件对象，迭代器，生成器，字典
（字典的迭代对键有效，并且由于字典的无序性，迭代结果无序）。
"""

# --------------------------------------------------------

"""
&& 普通解压 &&
变量数量必须与该可迭代对象的元素数量一致，一一对应。
将一个可迭代的对象通过赋值语句进行解压并将其元素赋值给多个变量。
"""

# 解压列表
test_data_1 = ['BigRabbit', 23, (2017, 12, 27)]
my_name, my_age, today_date = test_data_1
print(my_name)     # BigRabbit
print(my_age)      # 23
print(today_date)  # (2017, 12, 27)

# 解压元组
my_name, my_age, (this_year, this_month, this_day) = test_data_1
print(my_name)     # BigRabbit
print(my_age)      # 23
print(this_year)   # 2017
print(this_month)  # 12
print(this_day)    # 27

# 解压字符串
a1, a2, a3, a4, a5, a6, a7, a8, a9 = my_name
print(a1, a2, a3)       # B i g
print(a4, a5, a6, a7)   # R a b b

# 解压字典
# 由于普通字典的无序性，普通的字典不适合解压操作。普通解压对字典并没有太大意义。


# 解压的时候，使用占位符来代表不需要的值。  _  只能代表可迭代对象中的一个元素。
_, his_age, _ = test_data_1
print(his_age)    # 23

# --------------------------------------------------------

"""
&& * 星号表达式解压缩 &&
在解压可迭代对象时，用来接收值的变量的数量 少于 可迭代对象中元素的数量时，如果使用上面的方法会出现ValueError。
这时候可以在变量前面添加 * 来解决。 
"""

# 使用 * 的变量 始终都是列表类型
test_data_2 = [90, 95, 97, 99, 100]
min_num, *middle_num, max_num = test_data_2
print(min_num)      # 90
print(middle_num)   # [95, 97, 99]

*before_num, last_num = test_data_2
print(before_num)   # [90, 95, 97, 99]
print(last_num)     # 100


# 使用 * 解压字典
dict2 = {'year': 2017, 'month': 12, 'day': 27}
year, *others = dict2.items()
# year 的值不确定，('year', 2017)  ('month', 12) ('day', 27) 都有可能，解压没意义


# 可以使用 OrderDict 解压
from collections import OrderedDict
dict1 = OrderedDict()
dict1['year'] = 2017
dict1['month'] = 12
dict1['day'] = 27
print(dict1)        # OrderedDict([('year', 2017), ('month', 12), ('day', 27)])
i, *j = dict1.items()
print(i)            # ('year', 2017)
print(j)            # [('month', 12), ('day', 27)]


# 当你解压出一些元素又不想要他们，可以使用 *_ 或 *ign 或 *ignore

first_num, *_ = test_data_2
print(first_num)    # 90

"""
&& 判断一个对象是否是可迭代对象 &&
"""
# 可以使用collection中的Iterable和isinstance来判断一个对象是否可迭代，可以迭代则返回True,否则返回False
dict3 = {'country': 'China', 'city': 'beijing'}

from collections import Iterable
print(isinstance(dict3, Iterable))    # True

# ------------------------------------------------------------------------------

"""
&&  * 解压法 的一些用法  &&
"""

# 在字符串切割中使用 * 解压法
test_str = '/root/mycomputer;/templates;/usr/bin/files;/var/;/picture/image1;/docs'
dir1, *dir2, dir3 = test_str.split(';')
print(dir1)    # /root/mycomputer
print(dir2)    # ['/templates', '/usr/bin/files', '/var/', '/picture/image1']
print(*dir2)   # /templates  /usr/bin/files  /var/  /picture/image1   此处变量前面的 * 的作用是拆包
print(dir3)    # /docs

# 迭代列表，而列表的元素是不定长的元组（元组中元素个数不相同）

user_informations = [
    ('小A', 13123456789, '123@456.com'),
    ('小B', 15123456789),
    ('小C', '456@123.com')
]


def one_information(information):
    print(information)


def two_information(information1, information2):
    print('小A', information1, information2)


for name, *informations in user_informations:
    if name == '小A':
        two_information(*informations)      # 小A 13123456789 123@456.com
    else:
        one_information(*informations)      # 15123456789   456@123.com

# ----------------------------------------------------------------------------

# 上面主要是使用 * 号对可迭代对象部分拆包，亦可以使用 * 号对可迭代对象整体拆包。
""" &&如果不在变量名前加 * ,则该变量为一个列表。 如果在变量前加 * ，则对该列表进行拆包。&&
    比如下面的例子中 使用*args对[0, 1, 2, 3, 4, 5]进行拆包，
    args 表示一个列表， 
    *args表示列表拆包后的所有元素
"""

arg1, *args = [0, 1, 2, 3, 4, 5]
print(*args)    # 1 2 3 4 5
print(args)     # [1, 2, 3, 4, 5]


"""
&& 小结 &&
1、使用 * 解压语法可以专门解压不确定个数或任意个数元素的可迭代对象，通过 * 号解压出来的元素在一个列表中。

2、普通字典无序，解压没有意义。对有序字典OrderDict进行普通解压也 没有意义。一般对 OrderDict 进行 * 解压。

3、当你使用 * 解压出多个元素，但是又不想要这些元素，可以用 *_ 或者 *ign 或 *ignore。
"""