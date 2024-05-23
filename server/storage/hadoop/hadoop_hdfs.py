# from hdfs.client import Client
#
# client = Client("http://10.100.1.100:9870")
# print(client.list('/test'))
# print(client.list('/pytest'))

from hdfs import InsecureClient

# client = Client('http://10.100.1.100:9870')
# 连接服务器
client = InsecureClient('http://10.100.1.100:9870', user='qyoung')
# 创建目录test
client.makedirs('/test')
# 写入文件内容
client.write(hdfs_path='/test/1.txt', overwrite=True, data='hdfs你好，我来了'.encode('utf-8'))
# 上传文件
client.upload(hdfs_path='/test/pyvenv.cfg', local_path='pyvenv.cfg')
# 列出文件
print(client.list('/test'))
# 查看文件是否存在
print(client.status(hdfs_path='/test/pyvenv.cfg', strict=False))
# 查看文件内容
with client.read('/test/1.txt') as f:
    print(f.data.decode('utf-8'))

# 下载文件
client.download(hdfs_path='/test/1.txt', overwrite=True, local_path='2.txt')
# 重命名文件
client.rename('/test/1.txt', '/test/2.txt')
client.rename('/test', '/test1')
# 删除文件目录
client.delete('/test1/pyvenv.cfg')
client.delete('/test1/2.txt')
client.delete('/test')