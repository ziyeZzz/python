#-*- coding:utf-8 -*
'''
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

相当于26进制转10进制
'''
def titleToNumber(s):
    capacity = len(s)-1
    num_sum = 0
    for i in range(len(s)):
        num_sum += (ord(s[i])-ord('A')+1)*(26**(capacity-i))
    return num_sum

if __name__=='__main__':
    s = 'ZY'
    print(titleToNumber(s))
