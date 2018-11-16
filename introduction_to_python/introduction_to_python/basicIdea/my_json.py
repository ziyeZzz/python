# 定义一个字典
# a = {'name':"zz",'age':15}
# print(type(a))
# print(a['name'])
import json
json_str = '{"name":"zz","age":13}'
student = json.loads(json_str)
#将json字符串转换成了字典
print(type(student))
print(student)
print(student['name'])
print(student['age'])

#将json数组转换成了python中的list
json_array = '[{"name":"zz","age":13},{"name":"zzz","age":15}]'
student = json.loads(json_array)
print(type(student))
print(student,"hh")#只是试试怎么和字符串一起输出

#序列化：python->json, 反序列化：json(字符串)->python
#反序列化：json.loads
#序列化：json.dumps
#定义一个字典，用括号来实现换行。
student = [
            {'name':'zz','age':15,'flag':True},
            {'name':'zzz','age':17},
        ]
#dumps接受的参数是object,字典也是object，所以可以直接传进去
json_str = json.dumps(student)
print(type(json_str))
print(json_str)