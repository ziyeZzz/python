'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
def findKthLargest(nums, k):
    return quick_find(nums,0,len(nums)-1,len(nums)-k)

#利用快排partition
def quick_find(nums,left,right,k):
    if left<right:
        pivot = partition(nums,left,right)
        if pivot < k:
            return quick_find(nums, pivot + 1, right, k)
        elif pivot > k:
            return quick_find(nums,left,pivot-1,k)
        else:
            return nums[pivot]
    elif k==left:
        return nums[left]
    else:
        return None

#从大到小排序
def partition(nums,left,right):
    pivot_key = nums[left]
    while left<right:
        while left<right and nums[right]>=pivot_key:
            right-=1
        nums[left] = nums[right]
        while left<right and nums[left]<=pivot_key:
            left+=1
        nums[right] = nums[left]
    nums[left]=pivot_key
    return left

if __name__=='__main__':
    nums=[99,99]
    k=1
    print(findKthLargest(nums,k))
