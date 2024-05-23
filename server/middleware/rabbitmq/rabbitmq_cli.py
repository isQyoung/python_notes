import pika
import sys
import time

# 远程rabbitmq服务的配置信息
username = 'guest'  # 指定远程rabbitmq的用户名密码
pwd = 'guest'
ip_addr = '192.165.1.103'
port_num = 5672

credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(ip_addr, port_num, '/', credentials))
channel = connection.channel()


# 消费成功的回调函数
def callback(ch, method, properties, body):
    print(" [%s] Received %r" % (time.time(), body))
    # time.sleep(0.2)


# 开始依次消费balance队列中的消息
channel.basic_consume(queue='python_test', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 启动消费
