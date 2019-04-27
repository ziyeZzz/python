'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
'''
a="11";b="1"
def addBinary(a,b):
    # 补位
    if len(a)>len(b):
        b=(len(a)-len(b))*'0'+b
    else:
        a=(len(b)-len(a))*'0'+a
    nextAdd = 0
    result=""
    # 计算
    for i in range(len(a)-1,-1,-1):
        iSum = int(a[i])+int(b[i])+nextAdd
        if iSum>=2:
            nextAdd = 1
            result = str(iSum-2)+result
        else:
            nextAdd = 0
            result = str(iSum)+result
    if nextAdd:
        result = '1'+result
    return result
print(addBinary(a,b))