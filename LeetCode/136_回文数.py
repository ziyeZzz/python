'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
x = 121
def my_func(x):
    if x < 0:
        return False
    else:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False
print(my_func(x))