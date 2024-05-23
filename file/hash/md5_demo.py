import hashlib

# 需要哈希的字符串
passwd = '123456'
# md5 加盐 并哈希字符串,盐为空等于hashlib.md5()
salt = ''
m = hashlib.md5(salt.encode("utf-8"))
m.update(passwd.encode("utf-8"))
# 输出字符串
print(m.hexdigest())