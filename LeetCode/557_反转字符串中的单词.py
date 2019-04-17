'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''
s="Let take LeetCode contest"
def reverseWords(s):
    reverse_s=""
    list_s=s.split()
    for word in list_s:
        reverse_s += word[::-1]+' '
    return reverse_s.strip()

def reverseWords2(s):
    j=0
    rev_s=""
    s+=" "
    for i in range(0,len(s)):
        if s[i] == ' ':
            word=s[j:i]
            rev_word=""
            for m in range(len(word)-1,-1,-1):
                rev_word+=word[m]
            j = i+1
            rev_s += rev_word+' '
    return rev_s.strip()
print(reverseWords2(s))