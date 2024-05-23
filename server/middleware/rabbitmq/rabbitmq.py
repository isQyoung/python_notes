import pika
import sys
import time

# 远程rabbitmq服务的配置信息
username = 'guest'  # 指定远程rabbitmq的用户名密码
pwd = 'guest'
ip_addr = '192.165.1.102'
port_num = 5672

# 消息队列服务的连接和队列的创建
credentials = pika.PlainCredentials(username, pwd)
connection = pika.BlockingConnection(pika.ConnectionParameters(ip_addr, port_num, '/', credentials))
channel = connection.channel()
# 创建一个名为python_test的队列，对queue进行durable持久化设为True(持久化第一步)
channel.queue_declare(queue='python_test', durable=True)

message_str = 'Hello World!'
for i in range(1000):
    # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channel.basic_publish(
        exchange='',
        routing_key='python_test',  # 写明将消息发送给队列python_test
        body=message_str,  # 要发送的消息
        properties=pika.BasicProperties(delivery_mode=2)  # 设置消息持久化(持久化第二步)，将要发送的消息的属性标记为2，表示该消息要持久化
    )  # 向消息队列发送一条消息
    print(" [%s] Sent 'Hello World!'" % i)
    time.sleep(0.2)
connection.close()  # 关闭消息队列服务的连接
