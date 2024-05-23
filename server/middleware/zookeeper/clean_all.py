# 清空所有节点
from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.66.99:2181,192.168.66.99:2182,192.168.66.99:2183')
zk.start()

nodes = zk.get_children('/')  # 查看根节点有多少个子节点
print(nodes)
for i in nodes:
    if i != 'zookeeper':  # 判断不等于zookeeper
        print(i)
        # 删除节点
        zk.delete('/%s' % i, recursive=True)
zk.stop()  # 与zookeeper断开
