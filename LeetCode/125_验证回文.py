# -*- coding: utf-8 -*
'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''

def isPalindrome(s):
    # remove symbols
    s = s.lower()
    s = ''.join(filter(str.isalnum,s))
    i = 0
    j = len(s)-1
    while i<=j:
        if s[i] != s[j]:
            return False
        i = i+1
        j = j-1
    return True

if __name__=='__main__':
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print(isPalindrome(s))