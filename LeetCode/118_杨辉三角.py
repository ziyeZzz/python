'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(numRows):
    last_row = [1]
    this_row = []
    if numRows>0:
        print(last_row)
        for i in range(2,numRows+1):
            last_row = [0] + last_row + [0]
            for num in range(1,i+1):
                this_row.append(last_row[num-1]+last_row[num])
            print(this_row)
            last_row = this_row
            this_row = []

if __name__=='__main__':
    generate(5)
            
