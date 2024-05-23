from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

# 读取加密后的数据
file_in = open("data.encrypt", "rb")

# 读取RSA私钥
private_key = RSA.import_key(open("private.key").read())

# 获取加密后的session_key,以及nonce, tag, ciphertext
enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
file_in.close()

# 使用RSA私钥解密session key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# 使用AES session key 解密数据
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))