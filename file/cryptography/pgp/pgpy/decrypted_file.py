import pgpy

# 需要用的的文件和密码
PRIVATE_KEY_FILE = 'mykey.asc'
PASSPHRASE = '123456'
FILE_TO_DECRYPT = 'file.gpg'
OUTPUT_FILE = 'defile.txt'

# 从文件中加载私钥
priv_key, _ = pgpy.PGPKey.from_file(str(PRIVATE_KEY_FILE))

# 加载加密文件
encrypted_message = pgpy.PGPMessage.from_file(FILE_TO_DECRYPT)

# 使用密码解锁私钥
with priv_key.unlock(PASSPHRASE):
    # 在此处执行解密操作
    decrypted_message = priv_key.decrypt(encrypted_message)

# 将解密后的消息保存到文件中
with open(OUTPUT_FILE, 'w') as f:
    f.write(decrypted_message.message)