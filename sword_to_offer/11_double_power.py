# -*- coding:utf-8 -*-
# 此题最主要的是各种输入情况都要考虑到。如底数为0，指数为负时的错误处理。
'''
Q: 实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。
'''

# 一开始的直观思路，虽然快，但没有考虑指数等于0和负数情况
def double_power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result*base
    return result

# python内置幂运算方法
def double_power_byPython(base, exponent):
    return base ** exponent

# 将不同情况都考虑进去，如base=0,exp=0,exp<0
def double_power_2(base, exponent):
    if base==0:
        return 0
    elif exponent==0:
        return 1
    elif exponent < 0:
        exponent = -1 * exponent
        tmp = double_power(base, exponent)
        return 1/tmp
    else:
        return double_power(base, exponent)

# 效率更高的方法，优化幂运算过程。如x^32=x^16*x^16,x^16=x^8*x^8,...,x^2=x*x. 一共只需进行5次运算就可以算出。
# a^n = a^(n/2) * a^(a/2) n为偶数
#     = a^((n-1)/2) * a^((n-1)/2) * n n为奇数
# 未考虑 exp<0的情况
def double_power_opt(base, exponent):
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    result = double_power_opt(base, exponent>>1)
    result *= result
    if exponent&0x1 == 1:
        result *= base
    return result

if __name__=='__main__':
    print(double_power(2,-3))
    print(double_power_byPython(2, -3))
    print(double_power_2(2, -3))
    print(double_power_opt(2,3))