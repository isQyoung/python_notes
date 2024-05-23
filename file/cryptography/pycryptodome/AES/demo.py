from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

key = b'0123456789abcdef' # 密钥，长度必须为16、24或32字节
data = '123456' # 需要加密的数据

# 加密
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
encrypted_data = iv + ct

# 解密
iv = b64decode(encrypted_data[:24])
ct = b64decode(encrypted_data[24:])
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
decrypted_data = pt.decode()

print('加密后的数据:', encrypted_data)
print('解密后的数据:', decrypted_data)