from passlib.hash import pbkdf2_sha256

password = "mypassword"

# 使用pbkdf2进行哈希
hash1 = pbkdf2_sha256.hash(password)
print(hash1)
# 使用pbkdf2进行比对校验
if pbkdf2_sha256.verify(password, hash1):
    print("哈希1与密码匹配")
else:
    print("哈希1与密码不匹配")

hash2 = pbkdf2_sha256.hash(password)
print(hash2)
if pbkdf2_sha256.verify(password, hash2):
    print("哈希2与密码匹配")
else:
    print("哈希2与密码不匹配")
