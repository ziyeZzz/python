'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
'''
haystack = "hello"; needle = "ll"
def strStr(haystack,needle):
    #判断特殊输入
    if not needle:
        return 0
    if not haystack:
        return -1
    #两个字符串的长度
    needle_len = len(needle)
    haystack_len = len(haystack)
    #指针->haystack可能与needle相等的开始
    i = 0
    #若存在i开始，则长度肯定不超过haystack本身，可减少循环次数
    while i + needle_len - 1 < haystack_len:
        #若第一个字符相等
        if haystack[i] == needle[0]:
            #若切片相等
            if haystack[i:i + needle_len] == needle:
                return i
        i += 1
    return -1
print(strStr(haystack,needle))
