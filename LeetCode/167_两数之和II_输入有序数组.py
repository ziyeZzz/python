# -*- coding: utf-8 -*
'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

以下思路为：双指针。时间复杂度O(n)
另一思路为：固定一个数num，用二分查找法搜索target-num。时间复杂度O(nlogn)
'''
def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i<j:
        num_sum = numbers[i]+numbers[j]
        if num_sum==target:
            return i+1,j+1
        elif num_sum > target:
            j = j-1
        else:
            i = i+1
    return False

if __name__=='__main__':
    numbers=[2, 7, 11, 15]
    target = 9
    print(twoSum(numbers,target))