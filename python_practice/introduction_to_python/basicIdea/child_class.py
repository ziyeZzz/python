from parent_class import Human
#Student类继承Human类
class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        #Human.__init__(self, name, age)
        #子类调用父类的方法首选用super，而不是上面用类名并传入self的方法。因为用super后，如果后续需要改动，可直接改父类名字，而不用改子类内部实现。
        super(Student, self).__init__(name,age)

student1 = Student("High school","zz",12)
print(student1.age)
print(student1.name)
# print(student1.sum)
# print(Student.sum)
# student1.get_name()
