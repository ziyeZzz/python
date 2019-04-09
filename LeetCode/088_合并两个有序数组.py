'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
'''
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
def merge(nums1,m,nums2,n):
    nums1[m:]=nums2
    nums1.sort()
merge(nums1,m,nums2,n)
print(nums1)