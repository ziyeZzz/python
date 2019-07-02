'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
# 桶排序
def topKFrequent(nums,k):
    buckets = [0 for n in range(0,len(nums))]
    for num in nums:
        buckets[num]+=1
    for i in range(0,len(nums)):
        if buckets[i] > 0:
            return


if __name__=='__main__':
    nums=[1,1,1,1,2,2,3]
    k=2
    print(topKFrequent(nums,k))