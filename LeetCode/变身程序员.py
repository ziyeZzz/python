import sys
data=[]
for line in sys.stdin:
    values = list(map(int, line.split()))
    if values:
        data.append(values)
    else:
        break
#data=[[1,2,1],[1,1,0],[0,1,1]]
flag=True
ans=0
while flag:
    flag=False
    tmp=[]
    for row in range(0,len(data)):
        line = data[row]
        for col in range(0,len(line)):
            value=line[col]
            if value==1:
                if (col+1<len(line) and line[col+1]==2) \
                        or (col-1>=0 and line[col-1]==2)\
                        or (row-1>=0 and data[row-1][col]==2)\
                        or (row+1<len(data) and data[row+1][col]==2):
                    tmp.append([row,col])
                    flag=True
    for i in tmp:
        row=i[0]
        col=i[1]
        data[row][col]=2
    if flag:
        ans+=1
if ans>0:
    print(ans)
else:
    print(-1)