'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
例如：
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
'''
nums=[0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    # 如果nums不为空
    if nums:
        i = 0
        for n in nums:
            if n != nums[i]:
                i += 1
                nums[i]=n#覆盖之前的数
        return i+1
    else:
        return 0
print(removeDuplicates(nums))
