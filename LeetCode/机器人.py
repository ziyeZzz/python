import sys
import math
# n = int(sys.stdin.readline().strip())
# line=sys.stdin.readline().strip()
# nums = list(map(int, line.split()))
nums=[1,6,4]
#output=4
# 4 4 4-4
# 1 6 4-3
E=0
for i in range(len(nums)-1,0,-1):
    E=nums[i]
    if i>0:
        if nums[i]<nums[i-1]:
            m=nums[i-1]-nums[i]
            tmp=math.ceil(m*0.5)
            E1=E+tmp
            E2=E-tmp
            E=min(E1,E2)
print(E)