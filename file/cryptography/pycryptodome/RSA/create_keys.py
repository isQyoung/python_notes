from Crypto.PublicKey import RSA

# 生成2048位的密钥
key = RSA.generate(2048)
# 用密钥导出私钥
private_key = key.export_key()
file_out = open("private.key", "wb")
file_out.write(private_key)
file_out.close()

# 用私钥生成公钥
public_key = key.publickey().export_key()
file_out = open("public.key", "wb")
file_out.write(public_key)
file_out.close()