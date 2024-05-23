from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# 等待加密的数据data
data = "0123456789 - abcdefghijklmnopqrstuvwxyz".encode("utf-8")
print(data)

# 读取公钥,获取session_key
recipient_key = RSA.import_key(open("public.key").read())
#session_key = get_random_bytes(16)
session_key = b'\xf0\xe8\xe6\xcfV[XY\x9c\x1d\x9f\x90\xba\xdf\x0bv'

# 使用rsa公钥加密session_key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# 使用AES session key 来加密data
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
file_out = open("data.encrypt", "wb")
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
file_out.close()