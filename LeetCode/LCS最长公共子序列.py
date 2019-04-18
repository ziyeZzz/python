str1="1A2C3D4B56"
str2="B1D23CA45B6A"
def LCS(str1,str2):
    m=len(str1)
    n=len(str2)
    result = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                result[i][j]==result[i-1][j-1]+1
            else:
                result[i][j]=max(result[i-1][j],result[i][j-1])
    return result[-1][-1]
print(LCS(str1,str2))
