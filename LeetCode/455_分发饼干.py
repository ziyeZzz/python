'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。

示例 1:

输入: [1,2,3], [1,1]

输出: 1

解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
'''
def findContentChildren(g,s):
    QuickSort(g)
    QuickSort(s)
    count=i=j=0#两个指针分别小孩和饼干。遍历每块饼干，有最小够分给小孩的饼干就count加一。
    while i<len(g) and j<len(s):
        if g[i]<=s[j]:
            count+=1
            i+=1
        j+=1
    return count

def partition(nums,left,right):
    pivot_key = nums[left]
    while left<right:
        while left<right and nums[right]>=pivot_key:
            right-=1
        nums[left] = nums[right]
        while left<right and nums[left]<=pivot_key:
            left+=1
        nums[right] = nums[left]
    nums[left] = pivot_key
    return left
def quick_sort(nums,left,right):
    if left<right:
        pivot = partition(nums,left,right)
        quick_sort(nums,left,pivot-1)
        quick_sort(nums,pivot+1,right)

def QuickSort(nums):
    quick_sort(nums,0,len(nums)-1)

if __name__=='__main__':
    g=[10,9,8,7]
    s=[5,6,7,8]
    print(findContentChildren(g,s))