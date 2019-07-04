'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
#碰到0就放到前面，碰到1不管，碰到2放到后面
def sortColors(nums):
    i = 0#指1
    c = 0#当前
    j = len(nums)-1#指2
    while c <= j:
        #等于0时
        if nums[c]==0:
            #c和i不相等时，把c所指的0换到i所指的地方。因为此时i才有可能指向的是1
            if i!=c:
                tmp = nums[c]
                nums[c] = nums[i]
                nums[i] = tmp
            i+=1
            c+=1
        #c指1时，直接后移
        elif nums[c]==1:
            c+=1
        #c指2时，把c所指的2换到j所指的地方
        else:
            tmp = nums[c]
            nums[c] = nums[j]
            nums[j] = tmp
            j-=1
    return nums

if __name__=='__main__':
    nums=[2,0,2,1,0,1,0,1]
    print(sortColors(nums))