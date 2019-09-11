'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''
def compareMedian(nums1,nums2):
    i = j = len(nums1)/2-1
    while median_count <= median_index+1:
        if nums[i]<nums[j]:
            median_count += len(nums1)-i
            i = int((len(nums1)+i)/2)
            j = int(j/2) 
        elif nums[i] > nums[j]:
            i = int(i/2)
            j = int((len(nums2)+j)/2)
        # to do
        else:
            return

def findMedianSortedArrays(nums1, nums2):
    if len(nums1+nums2)%2==0:
        median_index = len(nums1+nums2)/2
        median_indexs = [median_index-1,median_index]
    else: median_indexs = [len(nums1+nums2)/2]

    median_index = int(len(nums1+nums2)/2)
    median_count
    

