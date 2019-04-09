'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''
strs=["dog","racecar","car"]
def my_func(strs):
    if len(strs) <1:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        # 找到最小长度的字符串
        # min_len = len(strs[0])
        # min_len_str=strs[0]
        # for i in strs:
        #     if len(i)<min_len:
        #         min_len=len(i)
        #         min_len_str=i
        min_len_str = min(strs)
        min_len = len(min_len_str)
        # 对比剩余字符串
        count=0
        for i in range(0,min_len):
            for j in strs:
                if j[i]!=min_len_str[i]:
                    return count
            count+=1
        return count
print(my_func(strs))



