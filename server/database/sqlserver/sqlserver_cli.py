import pymssql

# 从SQL Server数据库获取连接字符串
server = '192.168.1.100'
database = 'testdata'
username = 'sa'
password = '123456'

# 连接到数据库
conn = pymssql.connect(server, username, password, database)
# 创建游标
cursor = conn.cursor()

# 执行SQL查询
query = 'SELECT * FROM [devdataflow].[dbo].[AbcAutoLog]'
cursor.execute(query)

# 获取查询结果
result = cursor.fetchall()
for row in result:
    print(row)

# 关闭连接
conn.close()
