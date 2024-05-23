from pymongo import MongoClient

# 创建MongoDB客户端
#client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb://root:123456@localhost:27017/')

# 选择数据库
db = client['mydatabase']

# 选择集合（表）
collection = db['mycollection']

# 创建要插入的文档
document = {"name": "John", "age": 30}
document_many = [
    {"name": "Joe", "age": 29},
    {"name": "Lily", "age": 29},
    {"name": "Bob", "age": 25}
]

# 插入文档到集合
collection.insert_one(document)
# 插入多条
collection.insert_many(document_many)

# 查询集合中的所有文档
documents = collection.find()
# 遍历查询结果
print('查询所有')
for document in documents:
    print(document)

# 更新匹配条件的文档
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# 指定查询条件
print('查询年龄大于28岁的文档')
query = {"age": {"$gt": 28}}
# 执行查询
results = collection.find(query)
# 遍历查询结果
for result in results:
    print(result)

# 删除匹配条件的文档
collection.delete_one({"name": "John"})
# 指定删除条件
print('删除年龄大于40岁的文档')
query = {"age": {"$lt": 40}}
# 执行删除操作
result = collection.delete_many(query)

# 打印删除的文档数量
print("删除了 {} 个文档".format(result.deleted_count))
