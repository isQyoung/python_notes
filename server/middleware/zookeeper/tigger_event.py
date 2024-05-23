import time
from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.66.99:2181,192.168.66.99:2182,192.168.66.99:2183')
zk.start()


def test(event):
    print('触发事件')
    zk.set('/testplatform/test', b'qyoung')


if __name__ == "__main__":
    while True:
        a = zk.get('/testplatform/test', watch=test)
        print(a)
        time.sleep(3)
        # zk.set('/testplatform/test',b'hello')
        # zk.get('/testplatform/test',watch = test)
        # print("第二次获取value")
