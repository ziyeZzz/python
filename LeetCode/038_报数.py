'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。



示例 1:

输入: 1
输出: "1"
'''
n=4
def countAndSay(n):
    # 初始化第一个数
    nums="1"
    # i--轮数
    i=0
    while i < n-1:
        #j--当前数每位
        j=0
        # 数相同的数连续出现了几次
        count=0
        # 用来对比是不是相同的数
        p=nums[0]
        # 下一行的数
        nextNum=""
        while j < len(nums):
            if nums[j]==p:
                count+=1
            else:
                nextNum += str(count) + p
                p=nums[j]
                count=1
            j+=1
        nextNum += str(count) + p
        nums=nextNum
        i+=1
    return nums
print(countAndSay(4))

