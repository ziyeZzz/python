'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''
s="[])"
# 网友简洁版 执行用时 96ms
def isValid2(s):
    while '{}' in s or '[]' in s or '()' in s:
        s = s.replace('{}','')
        s = s.replace('[]','')
        s = s.replace('()','')
        return s==''

# 自己写的版  执行用时80ms
def isValid(s):
    if s=='':
        return True
    else:
        tmp = []
        seq = ['(','[','{']
        i = 0
        while i < len(s):
            if s[i] in seq:
                if s[i]=='(':
                    tmp.append(')')
                elif s[i]=='{':
                    tmp.append('}')
                else:
                    tmp.append(']')
                i += 1
            else:
                if tmp:
                    while i<len(s) and s[i] not in seq and tmp:
                        if s[i] != tmp.pop():
                            return False
                        i+=1
                else:
                    return False
        if tmp:
            return False
        else:
            return True
print(isValid(s))


