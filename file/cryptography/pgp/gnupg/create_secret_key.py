# 创建密钥对
import gnupg

# 创建一个GPG对象
gpg = gnupg.GPG()

# 生成密钥对的参数,邮件密码等
input_data = gpg.gen_key_input(
    subkey_type='RSA',
    key_length=4096,
    name_real="Example Key",
    name_comment='Example comment',
    name_email='test@example.com',
    passphrase='test123'
)

# 生成密钥对
key = gpg.gen_key(input_data)
print(key.fingerprint)
# 导出公钥，返回一个字符串
public_key = gpg.export_keys(key.fingerprint)
# 导出公钥，写入文件
with open('public_key.asc', 'w') as f:
    public_key_str = gpg.export_keys(key.fingerprint)
    f.write(public_key_str)

# 导出私钥，返回一个字符串
private_key = gpg.export_keys(key.fingerprint, True, passphrase='test123')
# 导出私钥，写入文件
with open('private_key.asc', 'w') as f:
    private_key_str = gpg.export_keys(key.fingerprint, True, passphrase='test123')
    f.write(private_key_str)
