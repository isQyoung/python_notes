import pymysql

# 打开数据库连接
db = pymysql.connect(host="192.168.66.99", user="root", password="123456", port=3306, database="server_db",
                     charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 创建表 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS test_table")
# 使用预处理语句创建表
creae_sql = "CREATE TABLE test_table ( FIRST_NAME  CHAR(20) NOT NULL, LAST_NAME  CHAR(20), AGE INT, SEX CHAR(5), INCOME FLOAT )"
cursor.execute(creae_sql)
# 插入数据到表test_table
# SQL 插入语句
inset_sql = "INSERT INTO test_table(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'Man', 2001), ('Li', 'fala',21, 'Woman', 1999)"
try:
    # 执行sql语句 提交到数据库执行
    cursor.execute(inset_sql)
    db.commit()
except:
    # 如果发生错误则回滚
    print("错误,回退")
    db.rollback()

# 从表test_table查询数据  SQL 查询语句
select_sql = "SELECT * FROM test_table WHERE INCOME > %s" % (1000)
try:
    # 执行SQL语句
    cursor.execute(select_sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
# 更新   SQL 更新语句
update_sql = "UPDATE test_table SET AGE = AGE + 1 WHERE SEX = '%s'" % ('Man')
try:
    # 执行SQL语句
    cursor.execute(update_sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    print("错误,回退")
    db.rollback()

# 删除    SQL 删除语句
delete_sql = "DELETE FROM test_table WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(delete_sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    print("错误,回退")
    db.rollback()

# 关闭数据库连接
db.close()
