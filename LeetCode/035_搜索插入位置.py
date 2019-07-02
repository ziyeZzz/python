'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
'''
nums=[3,5,7,9,10];target=8
# 自己写的二分法
def searchInsert(nums, target):
    left=0;right=len(nums)-1
    #用二分法在nums中找target
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
    # target不存在于nums
    # 此时left已经在target应该插入的位置左边或右边
    if nums[left]<target:
        return left+1
    else:
        #注意不是left-1，因为插入后target将取代left的位置，left后移
        return left

# 网友写的简单版
def searchInsert2(nums, target):
    left=0;right=len(nums)
    #用二分法在nums中找target
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid
        else:
            left=mid+1
    return left
print(searchInsert(nums,target))
