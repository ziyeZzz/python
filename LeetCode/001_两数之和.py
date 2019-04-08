# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# ***思路***：
# 使用字典，每读一个数，就在字典中查找是否有target减去这个数的key
# 如果没有：把该数的值存成字典的index，该数的index存成字典的value。@@此处是这个思路巧妙的地方，查找key可以直接找到
# 如果有：输出两个数的index
# 2+7 和 7+2是一样的，先把2存在dict中，再在读到7时，找到2.
# 算法复杂度：log(n)
def twoSum(nums, target):
    dict={}
    for index,num in enumerate(nums):
        another_num = target - num
        print(dict)
        if another_num in dict:
            return [dict[another_num],index]
        dict[num]=index
    return None

if __name__=='__main__':
    nums = [2,7,11,15]
    target = 13
    print(twoSum(nums,target))