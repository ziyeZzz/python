#map and reduce and filter
#reduce返回的是list, map和filter返回类似(map/filter object)需用list来转换返回类型便于输出查看
def square(x):
    return x*x
list_x = [1,2,3,4,5,6,7,8]

#用循环
for x in list_x:
    square(x)

#用map
r = map(square, list_x)
print(r)
print(list(r))

#map的优势，与lambda表达式结合
r = map(lambda x:x*x, list_x)
print(list(r))

#another example
list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6,7,8]
r = map(lambda x,y:x*x+y, list_x,list_y)
print(list(r))

#reduce -> 用来连续计算
from functools import reduce
List_x = [1,2,3,4,5,6]
#progress: (((1+2)+3)+4)+..
r = reduce(lambda x,y:x+y, list_x)
print(r)

# location = [(1,2),(2,-2),(-2,3),(3,4)]
# r = reduce(lambda x,y:(x+a),(y+b), location)
# print(r)

#filter,返回结果必须代表真和假
#要求，把所有0都剔除
list_x = [0,1,1,0,1,0]
r = filter(lambda x:True if x==1 else False, list_x)
r = filter(lambda x:x, list_x)#同上一个结果
print(list(r))

import re
list_u = ['a','B','v','F','e']
r = filter(lambda x:len(re.findall('[a-z]',x)), list_u)
print(list(r))