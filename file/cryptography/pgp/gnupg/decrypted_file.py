# 解密文件
import gnupg

# 创建一个GPG对象
gpg = gnupg.GPG()

# 读取私钥，导入GPG
key_path = 'private_key.asc'
import_result = gpg.import_keys_file(key_path)
# 信任这个密钥
# gpg.trust_keys(import_result.fingerprints[0], 'TRUST_ULTIMATE')
# print(import_result.fingerprints[0])


# 打开一个要解密的文件对象
encrypted_file = 'encrypted.gpg', 'rb'

# 创建一个解密后的文件
decrypted_file = 'decrypted.txt'

# 用私钥解密文件，写入文件,如果上面未信任此密钥则需要多加一个参数always_trust=True
with open('encrypted.gpg', 'rb') as f:
    decrypted_data = gpg.decrypt_file(f, passphrase='test123', output=decrypted_file)