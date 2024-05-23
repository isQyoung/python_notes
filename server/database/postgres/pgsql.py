import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT  # 创建数据库需要加此行

user = "postgres"
pwd = "123456"
port = 5432
host = "192.168.66.99"

# 创建数据库
conn = psycopg2.connect(database="postgres", port=port, host=host, user=user, password=pwd)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # 创建数据库需要加此行
cur = conn.cursor()
cur.execute("CREATE DATABASE test")
# cur.close()
# conn.close()

conn = psycopg2.connect(database="test", port=port, host=host, user=user, password=pwd)
cur = conn.cursor()
# 创建表
create_sql = "CREATE TABLE test_table(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL)"
cur.execute(create_sql)
# 新增数据 并提交
data = "5, 'len', 22"
insert_sql = "INSERT INTO test_table VALUES (%s)" % data
cur.execute(insert_sql)
conn.commit()
# 更新数据 并提交
update_sql = "UPDATE test_table SET name='qyf' WHERE id=5"
cur.execute(update_sql)
conn.commit()
# 查询数据
select_sql = "select * from test_table"
cur.execute(select_sql)
print(cur.fetchall())
# 删除数据 并提交
delete_sql = "DELETE FROM test_table WHERE id=5"
cur.execute(delete_sql)
conn.commit()
# 关闭游标连接
cur.close()
conn.close()
