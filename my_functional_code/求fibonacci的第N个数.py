# Author: BigRabbit
#  下午11:38


class Solution(object):
    """
    求斐波那契数列的第N个数，
    比如:
    从0开始的斐波那契数列，
    第一个数是0，第二个数是1，第三个数是1，第四个数是2...

    """
    def __init__(self, first_number=0, second_number=1):
        self.first_number = first_number
        self.second_number = second_number

    def fibonacci(self, n):
        number = 0
        while True:
            yield self.first_number
            number += 1
            self.first_number, self.second_number = \
                self.second_number, self.first_number + self.second_number
            if number == n:
                break

    def get_value(self, n):
        value_dict = {index+1: i for index, i in enumerate(self.fibonacci(n))}
        return value_dict[n]


test = Solution()
# 默认情况下斐波那契数列的第5个数
result1 = test.get_value(5)
print(result1)  # 3

# 默认情况下斐波那契数列的第11个数
# 因为前面的结果为第5个数的值，那么第二次执行将以第一次的结果为起始值
result2 = test.get_value(6)
print(result2)  # 55
