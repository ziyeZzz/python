a = "123"
len = len(a)
num = 0
for i in range(0, len):
    num = num + int(a[len-i-1])*(pow(10, i))
print(str(num))
print(int(a))