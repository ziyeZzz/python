#Human类是child_class.py中Student的父类
class Human():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
    
    def get_name(self):
        print(self.name)