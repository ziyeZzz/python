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