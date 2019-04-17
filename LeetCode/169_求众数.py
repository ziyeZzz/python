'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
import math
nums=[1,2,1,1,1,3,4]
# 网友解法
def majorityElement2(nums):
    count=1
    base=nums[0]
    for i in range(1,len(nums)):
        if nums[i]==base:
            count+=1
        else:
            count-=1
            if count==0:
                base=nums[i+1]
    return base
# 自己解法
def majorityElement(nums):
    nums.sort()
    n=math.ceil(len(nums)/2)
    return nums[n]
print(majorityElement2(nums))