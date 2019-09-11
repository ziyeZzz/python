# coding:utf-8
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

def lengthOfLongestSubstring(s):
    if s:
        max_length = 1
        cur_length = 1
        i = 0
        j = 1
        while j<len(s):
            if s[i] == s[j]:
                i += 1
            else:
                target = s[j]
                org_i = i
                for m in range(i+1,j):
                    if s[m] == target:
                        i = m+1
                        cur_length = j-i+1

                if i == org_i:
                    cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
            j += 1
        return max_length
    else:
        return 0

if __name__=='__main__':
    s="pwwkew"
    print(lengthOfLongestSubstring(s))





