'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
nums=[-2,1,-3,4,-1,2,1,-5,4]
# 网上同学极简代码
def maxSubArray2(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+max(nums[i-1],0)
    return max(nums)
# 自己写的
# 思想：只要前面加和大于0，则对后面的加法有帮助
def maxSubArray(nums):
    if nums:
        sum = 0
        max_sum = 0
        flag=False#判断是不是都是负数
        for num in nums:
            sum += num
            if sum <= 0:
                sum = 0
            else:
                flag=True#只要能进到这个分支，则表明至少有一个数不是负数
                if max_sum < sum:
                    max_sum = sum
        if flag:
            return max_sum
        else:#如果都是负数，则输出最小的负数
            return max(nums)
    else:
        return 0
print(maxSubArray(nums))