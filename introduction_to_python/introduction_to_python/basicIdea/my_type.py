#类型
#字典,枚举:enum,枚举就是一个类,所有的枚举类都是Enum的子类
#枚举在python中的本质还是一个类
#枚举类的变量名/标签 建议用大写,大写表示常量
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

#打印出的就是变量名VIP.BLACK，而不是1. 
#且不能有相同的标签名
#若不同的标签赋相同的值，后面的标签会被第一个值相同的标签覆盖，相当于第一个标签的别名。且遍历时，别名不会被打出来。除非遍历时将VIP->换成->VIP__members__或VIP__members__.items()
print(VIP.BLACK)

a = {'yellow':1,'green':2}
class b():
    yellow = 1
    green = 2
#但字典或用普通类的缺点在于：
#1，值可变； 2，没有防止相同值的功能
#e.g. a['yellow'] = 2

#获取枚举类型的数值
print(VIP.GREEN.value)
#获取标签名字,字符串
print(VIP.GREEN.name)
#表示枚举下面的一个类型
print(VIP.GREEN)
#通过枚举的名字可以找到对应的枚举类型

#枚举类型可以进行等于比较，但不能做大小比较
#result = VIP.GREEN > VIP.BLACK #报错
result = VIP.GREEN == VIP.GREEN #True
result1 = VIP.GREEN is VIP.GREEN #True

#IntEnum强制每个标签的值都是int型。(Enum则没有这个限制)
#unique是装饰器，如果加了这个装饰器那么不同标签赋相同值就会报错
from enum import IntEnum, unique

#与普通类型相比，对枚举类型实例化是没有意义的，因为其设计模式 是 单例模式。