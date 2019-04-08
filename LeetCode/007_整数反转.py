x=-1234
str_x = str(x)
if str_x[0] == '-':
    x = int('-'+str_x[::-1][:-1])
else:
    x = int(str_x[::-1])
if -2 ** 31 < x < 2 ** 31:
    print(x)
else:
    print(0)
