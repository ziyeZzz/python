'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
'''
x = 9
def mySqrt(x):
    if x<=1:
        return x
    r = x
    while r > x/r:
        # r不断逼近x/r，不断求平均
        r = (r+x/r)//2
    return int(r)
print(mySqrt(x))