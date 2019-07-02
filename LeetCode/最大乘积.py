'''
Q:给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)
eg：3 4 1 2 -> 24

'''
import sys
for line in sys.stdin:
    input_list = line.split()
    l = list(map(int, input_list))
    l.sort()
    n = len(l)
    if n<3:
        print(0)
    else:
        print(max((l[0]*l[1]*l[-1]),(l[-1],l[-2],l[-3])))
