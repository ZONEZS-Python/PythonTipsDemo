import json

# 将 json 文件读取成字符串
json_data = open('age.json').read()
# 对json数据解码
data = json.loads(json_data)
# data 的类型是 字典dict
print(type(data))
# 直接打印 data
print(data)
# 遍历字典
for k, v in data.items():
    print(k + ':' + str(v))

# <class 'dict'>
# {'age': '10', 'name': '20', 'height': '170'}
# age:10
# name:20
# height:170