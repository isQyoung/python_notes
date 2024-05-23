import sqlite3

# 连接sqlite3
con = sqlite3.connect(r"F:\sqlite3.db")
# 直接在内存上建立数据库
#con = sqlite3.connect("memory")
# 创建游标
cur = con.cursor()
# 创建表
create_sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
cur.execute(create_sql)
# 新增数据 并提交
data = "5, 'len', 22"
insert_sql = "INSERT INTO test VALUES (%s)" %data
cur.execute(insert_sql)
con.commit()
# 更新数据 并提交
update_sql = "UPDATE test SET name='haha' WHERE id=5"
cur.execute(update_sql)
con.commit()
# 删除数据 并提交
delete_sql = "DELETE FROM test WHERE id=5"
cur.execute(delete_sql)
con.commit()
# 查询数据
select_sql = "select * from test"
cur.execute(select_sql)
print(cur.fetchall())
# 回滚
#con.rollback()
# 先关闭游标，在关闭数据库
cur.close()
con.close()