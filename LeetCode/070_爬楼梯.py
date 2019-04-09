'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''
n=3
# 网友简洁版,不需要数组，直接两个数互相迭代
def climbStairs2(n):
    a=b=1
    while n-1:
        a,b=b,a+b
        n -= 1
    return b
# 自己写的版本
def climbStairs(n):
    a=[]
    a.append(0)
    a.append(1)
    a.append(2)
    if n>2:
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2])
    return a[n]
print(climbStairs(n))