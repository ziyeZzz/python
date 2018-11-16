''' 
if-else, input, snippet
 '''

#empty list can also be used as boolean
d =[]
if d:
    print('ss')

#if-else, input, convert type:int('11')
account = 'zzz'
password = '123'
print('please input account')
user_account = input()
print('please input password')
user_password = input()

if(user_account == account and user_password == password):
    print('login successful!')
else:
    print('Sorry!')


#snippet, can use Tab to choose the next part
a = True
if a:
    print('aa')
else:
    pass
#pass: 空语句，占位语句

#while-else:当while判断条件为false后，就会执行else
counter = 1
while counter<=10:
    counter += 1
    print(counter)
else:
    print("EOF")

a = [[1,2,3],(a,b,c)]
for x in a:
    for y in x:
        print(y)
        if y==2:
            break
#如果不想每次都换行，则print(y, end='')
#因为print默认end为'\n'

#0~9
for x in range(0,10):
    print(x)
#0,2,4,6,8.第三个是步长
for x in range(0,10,2):
    print(x, end='|')
#递减等差
for x in range(10,0,-2):
    print(x, end='|')

#间隔取值打印出1，3，5，7，for和切片 两种方法
a = [1,2,3,4,5,6,7,8]
for x in range(0,len(a),2):
    print(a[x],end='|')

b = a[0:len(a):2]
print(b)


for target_list in expression_list:
    pass

class classname(object):
    pass

def funcname(parameter_list):
    pass
