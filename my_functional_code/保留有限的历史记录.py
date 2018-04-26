# Author: BigRabbit
#  下午4:40

# 在你对一些可迭代对象的元素进行了一系列操作后，
# 你想保留一些最新的历史记录，那么你可以使用deque

# 这个方法适用于少量的数据，临时的操作等简单的场合，
# 如果你想保留一个论坛的最近的文章记录或者一个电商
# 平台的某个顾客的最近的购物记录，那么，deque可能
# 是不合适的。数据库才是更好的选择。


# 下面是一个小例子：
# 用于保留一个可迭代对象中符合条件的最新的５条记录

from collections import deque


def search(lines, pattern, history=5):

    """
    筛选符合条件的元素，存入deque
    :param lines: 待查询文件
    :param pattern: 筛选关键字
    :param history: 展示记录的数量
    :return: 包含符合条件的记录的内容
    """

    result = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            result.append(line)
    yield result


with open('test.txt', 'r') as f:
    for pattern_result in search(f, 'python'):
        for one_line in pattern_result:
            print(one_line)
