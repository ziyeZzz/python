# -*- coding:utf-8 -*-
# 此题主要是 大数溢出处理
'''
Q: 打印1到最大n位数
输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1，2，3。。。知道最大的3位数即999
'''

# 一开始直观思路，未考虑大数溢出
def print_to_ndigits(n):
    if n < 1:
        return 'Error: n < 1'
    max = 10**n
    for i in range(1,max):
        print(i)

# 升级：用数组表达大数。也可以用字符串表示大数，但需要要字符串模拟加法，比较复杂
def print_to_ndigits_2(n):
    if n < 1:
        return 'Error: n < 1'
    num = [0,1,2,3,4,5,6,7,8,9]
    if n == 1:
        return num
    if n > 1:
        return None






if __name__=='__main__':
    # print_to_ndigits(1)
    print_to_ndigits_2(2)