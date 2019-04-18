'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
'''
nums=[-1,0,3,5,9,12]
target=9
def search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid = int((l + r) / 2)
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1
print(search(nums,target))
