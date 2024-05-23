import pgpy

# 需要用到的文件
PUBLIC_KEY_FILE = 'mykey_pub.asc'
FILE_TO_ENCRYPT = 'file.txt'
OUTPUT_FILE = 'file.gpg'

# 从文件中加载公钥
pub_key, _ = pgpy.PGPKey.from_file(str(PUBLIC_KEY_FILE))

# 加密文件
f_t_e = pgpy.PGPMessage.new(str(FILE_TO_ENCRYPT), file=True)
encrypted_f_t_e = pub_key.encrypt(f_t_e)

# 将加密后的消息保存到文件中
with open(OUTPUT_FILE, 'w') as f:
    f.write(str(encrypted_f_t_e))