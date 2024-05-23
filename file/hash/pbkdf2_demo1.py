# 方法一使用hashlib
import hashlib
import binascii
import os

password = b'my_password'
salt = os.urandom(16)  # 生成一个16字节的随机盐

# 使用PBKDF2算法生成一个32字节的密钥
key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=32)

# 将盐和密钥转换为十六进制字符串并打印出来
salt_hex = binascii.hexlify(salt).decode()
key_hex = binascii.hexlify(key).decode()
print(f'Salt: {salt_hex}')
print(f'Key: {key_hex}')