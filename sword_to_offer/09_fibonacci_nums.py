#-*- coding: utf-8 -*-
'''
Q1: 写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
f(n) = 0 (n=0)
     = 1 (n=1)
     = f(n-1)+f(n+1) (n>1)
'''
def fibonacci_n(n):
    num = None

    if n == 0:
        num = 0
