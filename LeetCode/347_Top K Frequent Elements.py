'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
# 桶排序
def topKFrequent(nums,k):
    #先用哈希表统计每个数出现的次数
    map={}#key里存的是num，value存的是num的出现频率
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    # 因为数字出现频率不可能高于这个数组本身长度,但要注意需包含频率=len(nums),所以range这里要+1
    topN_bucket = [None for n in range(0,len(nums)+1)]
    #桶排序，num出现频率为桶下标，桶里装的是出现相同频率的num
    for key in map:
        if topN_bucket[map[key]]==None:
            topN_bucket[map[key]] = []#考虑有相同频率的num
        topN_bucket[map[key]].append(key)
    #倒序输出桶中的前k个num
    topK = []
    for bucket in topN_bucket[::-1]:
        if bucket!=None:
            topK+=bucket
            if len(topK)>=k:
                break
    return topK[:k]

if __name__=='__main__':
    nums=[1]
    k=1
    print(topKFrequent(nums,k))