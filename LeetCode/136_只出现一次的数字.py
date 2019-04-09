'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。
'''

def singleNumber(self, nums: List[int]) -> int:
    a = 0
    # 任何数与0相与为其自身，与其自身相与为0
    # 交换律：a ^ b ^ c <=> a ^ c ^ b
    #任何数于0异或为任何数 0 ^ n => n
    #相同的数异或为0: n ^ n => 0
    for i in nums:
        a = a ^ i
    return a