from kazoo.client import KazooClient

# 基本操作
zk = KazooClient(hosts='192.168.91.128:2181')  # 如果是本地那就写127.0.0.1
#  与zookeeper断开建立连接
zk.start()
# 查看节点
zk.get_children('/')  # 查看根节点有多少个子节点
# 创建节点
# makepath=True是递归创建,如果不加上中间那一段，就是建立一个空的节点
zk.create('/abc/JQK/XYZ/0001', b'this is my house', makepath=True)
# 更改节点
zk.set('/abc/JQK/XYZ/0001', b"this is your horse!")
# 删除节点
zk.delete('/abc/JQK/XYZ/0001', recursive=True)
# 与zookeeper断开
zk.stop()
