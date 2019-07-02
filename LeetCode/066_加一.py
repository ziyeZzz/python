'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
'''
digits=[1,2,3]
def plusOne(digits):
    addMore=1
    for i in range(len(digits)-1,-1,-1):
        sum = digits[i]+addMore
        digits[i] = sum%10
        addMore =sum//10
    if addMore:
        digits=[addMore]+digits
    return digits
print(plusOne(digits))
