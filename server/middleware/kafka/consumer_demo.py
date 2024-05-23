# kafka消费者
from kafka import KafkaConsumer
import json


def consumer_demo():
    consumer = KafkaConsumer(
        'kafka_demo',
        bootstrap_servers='192.168.66.99:9092',
        group_id='test'
    )
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
        )
        )


if __name__ == '__main__':
    consumer_demo()
