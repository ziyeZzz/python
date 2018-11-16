#装饰器,不改变原有函数，新增功能
import time
def decorator(func):
    #封装,表示参数为零或多个，也可以为空不写
    #但是args并没包括关键字参数，所以完整的写法要加上*kw
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)#也可以为空
    return wrapper

def f1():
    print("hhh")

#这种用法不完整
f = decorator(f1)
f()

#但装饰器真正的妙处，在于用@decorator
@decorator
def f2():
    print("hhh")
f2()
#有了这个@符号后，不需要改变原来函数的调用方式

@decorator
def f3(func_name):
    print("hhh"+func_name)
f3("zz")

@decorator
def f4(func_name1,func_name2):
    print("hhh"+func_name1+" "+func_name2)
f4("zz","haha")

@decorator
def f5(func_name1,func_name2, **kw):
    print("hhh"+func_name1+" "+func_name2)
    print(kw)
f5("zz","haha",a=1)

