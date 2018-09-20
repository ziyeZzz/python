#-*- coding: utf-8 -*-
# 此题主要是二分查找
# 旋转数组的最小数字, 解法：遍历，递归
'''
Q: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
 * 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
 * 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''

# 自己直观思路：遍历。找到比第一个数小的数则是最小数。复杂度O(n)
def find_min_number(list):
    if len(list) == 0:
        return 'Empty list'
    num = list[0]
    for i in list:
        if num > i:
            return i
    return num

# 书中升级思路：二分查找。取中间数和左右两边指针分别比较，每次比较都可移动一半的距离。
# 终止条件为左右指针相邻。此时第二个指针指向的即是最小数。复杂度O(logn)
def find_min_number2(list):
    if len(list) == 0:
        return 'Empty list'
    elif len(list) == 1:
        return list[0]
    else:
        start = 0
        end = len(list)-1
        while start+1 < end:
            mid = int((start + end) / 2)
            if list[mid] >= list[start]:
                start = mid
            else:
                end = mid
        return list[end]

if __name__ == '__main__':
    rotatedArray = [3,3,4,5,1,2]
    print(find_min_number(rotatedArray))
    print(find_min_number2(rotatedArray))