# coding:utf-8
'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
def countPrimes(n):
    primes = [1 for i in range(n)]# prime is 1
    count = 0
    for i in range(2,n):
        if primes[i]:
            for j in range(i+i,n,i):
                primes[j] = 0
            count += 1
    return count

if __name__=='__main__':
    n = 10
    print(countPrimes(n))
