'''
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
'''
def diffWaysToCompute(input):
    opt = {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}
    result=[]
    #因为最后一个input的char肯定是数字，所以不用进行判定，len(input)-1
    for index in range(0,len(input)-1):
        #如果是operator
        if input[index] in opt:
            #左边所有计算方法的值
            for left in diffWaysToCompute(input[0:index]):
                #右边所有计算方法的值
                for right in diffWaysToCompute(input[index+1:]):
                    #左右分别用Operator操作
                    result.append(opt[input[index]](left,right))
    #如果result是空
    if not result:
        result.append(int(input))
    return result

if __name__=='__main__':
    input = "2*3-4*5"
    print(diffWaysToCompute(input))



