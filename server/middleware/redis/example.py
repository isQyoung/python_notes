# !/usr/bin/python3

import redis, uuid

# 创建redis连接池
pool = redis.ConnectionPool(host='172.16.5.201', port=6379, password=123456, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# 写入200个键值对到redis
for i in range(200):
    value = str(uuid.uuid4()).replace('-', '').upper()
    r.set('key_id' + str(i), value)
# 读取200个键值对
for i in range(200):
    print(r.get("key_id" + str(i)))
