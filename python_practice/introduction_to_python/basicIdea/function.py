import sys
#set recursion max times. Otherwise the default recursion times is 995
sys.setrecursionlimit(100000)

def add(x,y):
    return x+y
#可直接指定关键字参数,用与形参不同的顺序
c=add(y=3,x=2)
print(add(1,2))
#非默认参数必须全部放在默认参数前面
def print_info(name, gender='female', age='18'):
    print('My name:'+name)
    print('My gender:'+gender)
    print('My age:'+str(age))

print_info('zz','female',12)
print('~~~~~~~~~~~~~~~~~~')
print_info('zz2')
print('~~~~~~~~~~~~~~~~~~')
print_info('zz3',age=15)

a = 1
b = 2
c = 3
#可简写为：
a,b,c = 1,2,3

d = 1,2,3
#tuple
print(type(d))
a,b,c = d
a=b=c=1

#list
e = [1,2]
print(type(e))