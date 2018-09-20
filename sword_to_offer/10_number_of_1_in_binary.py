# -*- coding:utf-8 -*-
# 此题主要是位移符号的掌握，还有一个二进制神奇魔法（自身与减一相与）
'''
Q：请实现一个函数，输入一个整数，输出该二进制表示中1的个数。
例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
'''
# 注：不需要将十进制转换成二进制，它在运算时自己会自动转成二进制。反而如果用bin()转换，会导致得到的是str型。

# 末位与1进行与&运算，然后右移。1可以看成00001，无限补0。只有末位是1时，与1相与才会得到1，否则为0.
def count1(num):
    count = 0
    if num < 0:
        num = num*(-1)
    while num:
        count += num & 1
        num = num >> 1
    return count

# 改变思路：移动1，第一次0001，第二次0010，第三次0100。。。每次也是与num的一位进行与运算&比较。
# 虽然这种思路不需要对num判断正负，但它会需要将1移动至最大位数才结束循环。效率低。
def count1_update(num):
    count = 0
    flag = 1
    while flag:
        if flag & num > 0:
            count += 1
        flag = flag << 1
        print(count)
    return count

# 神奇思路
# 二进制，将它减1和它自身相与&，会使得最右边1变为0，有多少1就循环多少次，直到全为0为止。
def count2(num):
    if num < 0:
        # 负数,将最高位的符号位取反就可以得到补码。通常与0xFFFFFFFF相与得来。
        # 没明白，我选择乘以-1
        num = num * (-1)
    count = 0
    while num:
        count += 1
        num = (num-1)&num
    return count

# 人生苦短，我用python.@w@
def count3(num):
    return bin(num).count('1')

if __name__=='__main__':
    print(count1(-9))
    # print(count1_update(9))
    print(count2(-9))
    print(count3(-9))