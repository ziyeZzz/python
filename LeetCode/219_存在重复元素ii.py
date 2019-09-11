# coding:utf-8
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
'''
# 此解法最直观，但提交时超出时间限制
def containsNearbyDuplicate2(nums, k):
    for i in range(len(nums)-1):#the last number does not need to compare
        for j in range(i+1,i+k+1):
            if j < len(nums) and nums[i]==nums[j]:
                return True
    return False

# 空间换时间
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            if i - dic[nums[i]] <= k:
                return True
        dic[nums[i]] = i
    return False


if __name__=='__main__':
    nums = [1,2,3,1]
    k = 3
    print(containsNearbyDuplicate(nums,k))