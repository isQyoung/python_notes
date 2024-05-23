# 加密文件
import gnupg

# 创建一个GPG对象
gpg = gnupg.GPG()

# 导入公钥
key_path = 'public_key.asc'
import_result = gpg.import_keys_file(key_path)
# 信任这个密钥
gpg.trust_keys(import_result.fingerprints[0], 'TRUST_ULTIMATE')
# print(import_result.fingerprints[0])

# 打开一个要加密的文件对象
plain_file = 'plain.txt'

# 创建一个加密后的文件
encrypted_file = 'encrypted.gpg'

# 用密钥指纹找到公钥加密文件，如果上面未信任此密钥则需要多加一个参数always_trust=True
with open(plain_file, 'rb') as f:
    encrypted_data = gpg.encrypt_file(f, recipients=import_result.fingerprints[0], output=encrypted_file)
