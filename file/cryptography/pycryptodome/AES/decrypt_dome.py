from Crypto.Cipher import AES

# 从文件中读取加密后的数据
file_in = open("file.encrypt", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
file_in.close()

# 用来加解密的key
key = b'\xcc\xbb\xa2\x81\xde\x18 )x\xb1\xcc\xf7\xa9~<\xe1'
# 使用AES的EAX模式解密
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)