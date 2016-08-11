#this file is purely for testing purpose

import logging, time

from kafka import KafkaProducer

if __name__ == "__main__":
    logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
    )

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    producer.send('craw-url', b"test")
    producer.send('craw-url', b"\xc2Hola, mundo!")
