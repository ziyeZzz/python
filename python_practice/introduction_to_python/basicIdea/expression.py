#正则表达式
a = 'C,C++,Java, Python1, Python2, Javascript'
#判断a中是否有python
print(a.index('Python')>-1)
print('Python' in a)

#用正则表达式
import re
r = re.findall('Python', a)
print(r)
if len(r)>0:
    print('yes')
else:
    print('no')

b = 'a1b2c3d4'
# 'python' 普通字符, '\d' 元字符
#用正则表达式，简洁优美
r = re.findall('\d',a)
print(r)

#下面两个solution是用for循环
for char in b:
    try:
        print(int(char))
    except ValueError:
        pass

for char in b:
    if char.isdigit():
        print(char)

s = 'abc, acc, adc, aec, afc, ahc'
#抽象集，找出a c中间是c或f的字符串
r = re.findall('a[cf]c',s)
#取反
r = re.findall('a[^cf]c',s)
#区间
r = re.findall('a[c-f]c',s)
print(r)

#概括字符集
#e.g. '\d'数字, '\D'非数字
a = 'python111haha222'
r = re.findall('\d',a)
r = re.findall('[0-9]',a)#与\d同样的效果
r = re.findall('[^0-9]',a)#与\D同样的效果
print(r)

#\w, 所有字母与数字（单词字符）[A-Za-z-0-9_]
#\W, 所有非单词字符，包括空格，&，\n,\t...
#\s, 空白字符 \S 非空白字符
# ., 匹配除换行符\n外所有字符
#正则表达式只能匹配每一个字符

#数量词
a = 'python 111java222php'
#贪婪模式，取最大区间6
r = re.findall('[a-z]{3,6}',a)
#非贪婪模式，取最小3
r = re.findall('[a-z]{3,6}?',a)
print(r)

# *, (星号前的字符)匹配0次或无限多次
# +，(加号前的字符)匹配1次或无限多次
# ?，(加号前的字符)匹配0次或1次
a = 'pytho0python1pythonn2'
r = re.findall('python+',a)

#边界匹配,完整匹配整个字符.前面加^:从字符串开始。后面加$：从字符串末尾
qq = '100001'
#4~8
r = re.findall('^\d{4,8}$',qq)

#组 重复
a = 'PythonPythonPythonPython'
r = re.findall('(Python){3}',a)
#[abc] 与(a,b,c). 前者是或关系，后者是且关系，即必须全部出现。

#匹配模式， 第三个参数
language = 'PythonC#\nJavaPHP'
#先匹配c#， 再任意一组'.'
r = re.findall('c#.{1}', language, re.I|re.S)#忽略大小写 且 点号将匹配所有字符包括换行符
print(r)

#替换
language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#','GO',language,2)#2表示最多替换两次
print(r)
r = language.replace('C#','GO')
print(r)
#sub第二个参数可以是函数
def convert(value):
    return "!!"+'!!'
r = re.sub('C#', convert, language)
print(r)

#传入的value是object类型
def convertValue(value):
    matched = value.group()
    if int(matched)>5:
        return '9'
    else:
        return '0'
a = 'abc123de6712s'
r = re.sub('\d',convertValue, a)
print(r)

a = 'A83C72D8E78'
#match:从第一个字符开始比对不对
r = re.match('\d',a)#返回none
#search：搜索字符串直找到第一个满足正则表达式的为止
r1= re.search('\d',a)#返回object，1
print(r1.group())#8
print(r1.span())#0,1. 返回位置
#findall: 找出所有满足的
r2 = re.findall('\d',s)#返回[8,3,7,2,8,7,8]

#group
s = 'life is short, I use python'
r = re.search('life(.*)python',s)
print(r.group(1))

r = re.findall('life(.*)python',s)
print(r)
r = re.findall('life (\D)',s)
print(r)

s = 'life is short, I use python, I love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group(0))#全部
print(r.group(1))#第一个组，也就是（）括起来的东西
print(r.group(2))#第二个组，第二个（）括起来的
