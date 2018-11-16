#匿名函数lambda
def add(x,y):
    return x+y
print(add(1,2))

#lambda表达式，但这种调用方式并不好
#传入参数：内部表达式作为返回值
f = lambda x,y: x+y
print(f(1,2))

#三元表达式
#e.g. if x>y: return x, else return y
#在其他很多语言中用 x>y ? x:y 来表达。
#在python中：条件为真时返回的结果 if 条件判断 else 条件为假时的结果
x = 2
y = 1
r = x if x>y else y
print(r)
