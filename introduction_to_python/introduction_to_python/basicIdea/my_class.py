class Student():
    #类变量
    # name = 'zz'
    # age = 0
    s_sum = 0

    #构造函数,当实例化时，会自动运行init函数
    #但init函数，除了None不能返回别的值
    def __init__(self, name, age):
        #实例变量
        #初始化对象的属性
        self.name = name
        self.age = age
        #调用类变量
        self.__class__.s_sum +=1
        print('student:'+str(Student.s_sum))
        print('sum:'+str(self.__class__.s_sum))
    #实例方法
    def do_homework(self,mark):
        self.__mark = mark
        print('homework:'+mark)

    #类方法,与实例方法用self不同，类方法用cls(建议，用self也行)，还需在上面加上@classmethod
    #类方法主要用来操作与类相关的方法
    @classmethod
    def plus_sum(cls):
        cls.s_sum +=1
        print(cls.s_sum)

    #静态方法,静态方法中不需要传入self/cls
    @staticmethod
    def add(x,y):
        print(x+y)

    #静态方法和类方法不能直接调用实例变量, e.g. self.name


#类中写的函数和直接在模块中写的函数定义不一样，类中需要加上self
    def print_info(self):
        print('name is:'+self.name)
        print('age:'+str(self.age))

    #当方法/变量由双下划线开头，则会认为它是private。否则默认为public。
    #此规则除了构造函数（因为构造函数后面还有双下划线，因锤斯听）

    #当强行调用私有方法，则会报错
    #但当强行给私有变量赋值，则不会报错，会当作给实例新添加了一个变量（公开的）
    #注：python可以只有用点的方式定义新变量


student1 = Student('zzz',18)
#类方法可以被类及对象来调用。但建议不要用对象来调用类方法
Student.plus_sum()
#静态方法可以被类及对象来调用
Student.add(1,2)
student1.add(1,2)


#构造函数也可以直接被调用
#a = student1.__init__('zz',18)
student1.print_info()

#私有变量mark，如果用下面65行这种方式则会重新定义一个新的公开变量叫__mark
#因为python把我们之前定义的私有变量改了名字成_Student__mark。然而，通过写完整名字（改完后的名字）也是可以改变私有变量的。doge face
#严格意义上来讲，python中没有私有变量
student1.do_homework("yes")
student1.__mark = "yes"
student1._Student__mark = "no"

#dict可以打印出该对象实例所有的变量，成员列表
print(student1.__dict__)



