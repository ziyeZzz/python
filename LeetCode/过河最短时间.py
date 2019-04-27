import sys
# 读取第一行的n
n = int(sys.stdin.readline().strip())
for i in range(n):
    ans = 0
    # 读取每一行
    people_num = int(sys.stdin.readline().strip())
    people_line=sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    left = list(map(int, people_line.split()))
    left.sort()
    if people_num<4:
        ans=left[-1]
    else:
        min_time=left[1]
        i=people_num
        while i>3:
            ans+=left[i-1]+min_time
            i-=1
        ans+=left[2]
    print(ans)