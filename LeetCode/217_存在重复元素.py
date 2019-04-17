'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''
nums=[1,2,3,1]
# 网友用set
def containsDuplicate2(nums):
    nums_s=set(nums)
    if len(nums_s)==len(nums):
        return False
    else:
        return True
# 自己写的
def containsDuplicate(nums):
    nums.sort()
    pre=None
    for num in nums:
        if num==pre:
            return True
        else:
            pre=num
    return False
