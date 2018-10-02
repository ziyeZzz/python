#-*- coding: utf-8 -*-
# 此题主要是 斐波那契数列，f(n) = f(n-1) + f(n-2)
'''
Q1: 斐波那契数列
写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
f(n) = 0 (n=0)
     = 1 (n=1)
     = f(n-1)+f(n-2) (n>1)
'''
import time

#使用数组，将斐波那契数列存起来。
def fibonacci_n(n):
    list = [0,1]
    if n < 0:
        return 'Error: n < 0'
    elif n <= 1:
        return list[n]
    else:
        for i in range(2,n+1):
            next_num = list[i-1] + list[i-2]
            list.append(next_num)
        print(list)
        return list[n]

#不占用额外存储空间，使用prev1和prev2来存前两个数, 比第一个方法更高效。因为不用写入数组。
def fibonacci_n2(n):
    prev1 = 0
    prev2 = 1
    if n < 0:
        return 'Error: n<0'
    elif n == 1:
        return prev1
    elif n == 2:
        return prev2
    else:
        for i in range(2, n+1):
            next_num = prev1 + prev2
            prev1 = prev2
            prev2 = next_num
        return prev2

# 递归，虽代码简洁，但是因没保存之前的结果，会导致多次重复计算。性能不佳
def fibonacci_n3(n):
    if n < 0:
        return 'Error: n<0'
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_n3(n-1) + fibonacci_n3(n-2)


if __name__=='__main__':
    time_start = time.time()
    print(fibonacci_n(1000))
    time_end = time.time()
    print('original time:', time_end - time_start)
    time_start = time.time()
    print(fibonacci_n2(1000))
    time_end = time.time()
    print('no extra space cost time:', time_end - time_start)
    time_start = time.time()
    print(fibonacci_n3(30))
    time_end = time.time()
    print('recursion cost time:', time_end - time_start)


