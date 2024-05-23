from Crypto.Cipher import AES

# from Crypto.Random import get_random_bytes

# 用来加密的数据
data = b'123456789'

# 用来加解密的key
# key = get_random_bytes(16)
key = b'\xcc\xbb\xa2\x81\xde\x18 )x\xb1\xcc\xf7\xa9~<\xe1'
# 使用AES的EAX模式加密
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

# 把加密后的数据放到文件里
file_out = open("file.encrypt", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
file_out.close()
