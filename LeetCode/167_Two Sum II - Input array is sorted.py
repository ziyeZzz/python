'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

# 用这种一个一个查找的方法，如果前面有n个0，时间复杂度会超
def twoSum(numbers,target):
    i = 0
    j = 1
    while i<len(numbers):
        num1 = numbers[i]
        if num1 > target/2:
            break
        num2 = target - num1
        while j<len(numbers):
            if numbers[j] == num2:
                return [i+1,j+1]
            elif numbers[j] > target:
                break
            else:
                j+=1
        i+=1
        j=i+1
    return None

# 用字典的方法
def twoSum2(numbers,target):
    numbers_dict = {}
    for index, num in enumerate(numbers):
        num2 = target-num
        if num2 in numbers_dict:
            return [numbers_dict[num2]+1,index+1]
        numbers_dict[num] = index
    return None

# two pointer
def twoSum3(numbers,target):
    i = 0
    j = len(numbers)-1
    while i<j:
        two_sum = numbers[i] + numbers[j]
        if two_sum == target:
            return [i+1,j+1]
        elif two_sum < target:
            i+=1
        else:
            j-=1
    return None

if __name__=='__main__':
    numbers = [2,3,4]
    target = 6
    print(twoSum2(numbers,target))