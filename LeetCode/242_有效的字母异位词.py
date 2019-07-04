'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
说明:你可以假设字符串只包含小写字母。

进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    else:
        #结果字典
        dic = {}
        #先遍历s，数每个字符出现的次数，存在字典dic中，key是字符，value是出现次数
        for i in s:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        #遍历t，遇见相同字符，就在dic中减一；遇见不同字符，直接返回false
        for i in t:
            if i in dic:
                dic[i] -= 1
            else:
                return False
        #遍历结果字典，是否每个value都为0
        for i in dic:
            if dic[i] != 0:
                return False
    return True

if __name__=='__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))
