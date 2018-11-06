# -*- coding:utf-8 -*-
# 此题主要是 两个指针分别指向前后，同时移动并交换数据，以达到不需要额外空间的目的
'''
Q: 调整数组顺序使奇书位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇书位于数组的前半部分，所有偶数位于数组的后半部分
'''

# 判断奇偶可以用 num&1==0 偶
# 自己直观思路，分成奇偶数组再合并。但很明显这样会耗用更多的存储空间
def reorder_1(array):
    array_odd = []
    array_even = []
    for num in array:
        if num&1 == 0:
            array_even.append(num)
        else:
            array_odd.append(num)
    return array_odd+array_even

# 升级思路，两个指针p1,p2一前一后同时向中间移，在当前数组中交换指针指的数字（p1指奇则移，p2指偶则移），
# 停止条件为p2在p1前面
def reorder_2(array):
    p1 = 0
    p2 = len(array) -1
    while p2 > p1:
        if array[p1] & 1 == 0 and array[p2] & 1 == 1:
            tmp = array[p1]
            array[p1] = array[p2]
            array[p2] = tmp
        if array[p1] & 1 == 1:
            p1 += 1
        if array[p2] & 1 == 0:
            p2 -= 1
    return array


if __name__=='__main__':
    a = [1,2,3,4,5,6]
    print(reorder_1(a))
    print(reorder_2(a))
