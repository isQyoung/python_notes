import paramiko
import configparser

# 读取配置文件
conf = configparser.ConfigParser()
conf.read("config", encoding="utf-8")

# 创建临时文件
file = conf.get("file", "source")
num = conf.get("file", "size")
with open(file, 'w') as f:
    for _ in range(int(num)):
        f.write("0")


# 将本地 api.py 上传至服务器 /www/test.py。文件上传并重命名为test.py
count = conf.get("host", "count")
for i in range(1,int(count)+1):
    # 获取SSHClient实例 
    client = paramiko.SSHClient()
    # 将信任的主机自动假如到host_allow列表，需放在connect方法前面
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端
    client.connect(conf.get("host", "ip"), port=conf.get("host", "port"), 
                   username=conf.get("host", "username"), password=conf.get("host", "password"))
     # 获取Transport实例
    transport = client.get_transport()

    # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
    sftp = paramiko.SFTPClient.from_transport(transport)

    src=file
    dst = "{}/test{}".format(conf.get("file", "destination"),i)
    print(src,dst)
    sftp.put(src,dst)
    # 关闭连接
    client.close()

