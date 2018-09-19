#-*- coding: utf-8 -*-
'''
 Q:跳台阶
 * 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
 * 求该青蛙跳上一个n级的台阶总共有多少种跳法
'''
# 可以转换成斐波那契数列问题。见09_fibonacci_nums.py
# 青蛙跳上第0级台阶，不动=1种方法=1
# 青蛙跳上第1级台阶，从0级跳上来=1种方法=1
# 青蛙跳上第2级台阶，从0级跳上来或从1级跳上来=从0级跳上来方法总和+从1级跳上来方法总和=1+1=2
# 青蛙跳上第3级台阶，从1级跳上来方法总和+从2级跳上来方法总和。1+2=3
# ....
# 借用斐波那契数列规律，f(n) = f(n-1) + f(n-2)
def frog_jump(n):
    prev1 = 1
    prev2 = 1
    if n < 0:
        return 'Error: n<0'
    elif n == 0:
        return prev1
    elif n == 1:
        return prev2
    else:
        for i in range(2,n+1):
            next_num = prev1 + prev2
            prev1 = prev2
            prev2 = next_num
        return next_num

if __name__=='__main__':
    print(frog_jump(10))
