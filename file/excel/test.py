import re
import json
import tablib
import xlwt

# 读取文件内容
with open('2.txt', 'r', encoding='utf-8') as file:
    content = file.read().strip()
    # print(type(content))
    # print(content)

# 匹配 JSON 对象的正则表达式模式
pattern = r'({.*?})'

# 查找所有匹配的 JSON 对象
json_objects = re.findall(pattern, content)

data = []
# 获取第一行，读取键作为列标题
first_line = json.loads(json_objects[0])
headers = tuple([i for i in first_line.keys()])
print(headers)
data.append(headers)
# 解析每个 JSON 对象为 Python 字典
for obj in json_objects:
    json_data = json.loads(obj)
    # print(json_data)
    # print(type(json_data))
    body = []
    for v in json_data.values():
        body.append(v)
    data.append(tuple(body))


# 构造表格数据
all_data = tablib.Dataset(*data)

# 创建 Workbook 和 Worksheet
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
# 将数据写入 Worksheet
for i, row in enumerate(all_data):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)

# 保存为文件
workbook.save('data.xls')
