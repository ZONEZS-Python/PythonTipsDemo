# 下面编写代码对上面 country.xml 的 xml 进行解析，解析之后再分别格式化成字典和 json 格式的数据输出：
# XML 格式的数据既便于机器读取，也便于人工读取。
# 但是对于 xml 来说，预览并理解 CSV 文件和 JSON 文件要比 XML 文件容易得多。

# xml 格式说明：(针对 country.xml 中的电影数据做解释)

# Tag： 使用<和>包围的部分；
# Element：被Tag包围的部分，如 2003，可以认为是一个节点，它可以有子节点；
# Attribute：在Tag中可能存在的 name/value 对，如示例中的 title="Enemy Behind"，一般表示属性。


from xml.etree import ElementTree as ET  # 缩写名ET作用域仅限在本模块中引用
import json

tree = ET.parse('country.xml')

print(tree)

root = tree.getroot()

all_data = []

for movie in root:
    # 存储电影数据的字典
    movie_data = {}
    # 存储属性的字典
    attr_data = {}
    
    # 取出 type 标签的值
    movie_type = movie.find('type')
    attr_data['type'] = movie_type.text

    # 取出 format 标签的值
    movie_format = movie.find('format')
    attr_data['format'] = movie_format.text

    # 取出 year 标签的值
    movie_year = movie.find('year')
    if movie_year:  # 判断是否存在 ‘year’ 标签关键字，否则会存在报错
        attr_data['year'] = movie_year.text
    
    # 取出 rating 标签的值
    movie_rating = movie.find('rating')
    attr_data['rating'] = movie_rating.text

    # 取出 stars 标签的值
    movie_stars = movie.find('stars')
    attr_data['stars'] = movie_stars.text

    # 取出 description 标签的值
    movie_description = movie.find('description')
    attr_data['description'] = movie_description.text

    print('---' * 40)

    print(attr_data)

    # 获取电影名字，以电影名为字典的键，属性信息为字典的值
    movie_title = movie.attrib.get('title')
    movie_data[movie_title] = attr_data
    # 存入列表中
    all_data.append(movie_data)

# print(all_data)

print('***' * 40)

# all_data 此时是一个列表对象，用 json.dumps() 将Python对象转换为 json 字符串
json_str = json.dumps(all_data)

print(json_str)
