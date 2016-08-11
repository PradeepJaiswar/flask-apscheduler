import logging, time
from kafka import KafkaConsumer

from crawl_worker import crawl
from config.env import get_config
from app.constants import constants as COMMON_CONSTANTS

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )

consumer = KafkaConsumer(bootstrap_servers=get_config().KAFAK_BOOSTRAP_SERVERS,
                         auto_offset_reset=get_config().KAFKA_AUTO_OFFSET_REST)

while True:
    consumer.subscribe(['craw-url'])
    for message in consumer:
        crawl.delay(message)
