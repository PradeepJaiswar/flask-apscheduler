import logging, time
from kafka import KafkaConsumer

from workers.crawl_worker import crawl
from config.env import get_config
from app.constants import constants as COMMON_CONSTANTS

consumer = KafkaConsumer(bootstrap_servers=get_config().KAFAK_BOOSTRAP_SERVERS,
                         auto_offset_reset=get_config().KAFKA_AUTO_OFFSET_REST)

while True:
    consumer.subscribe(COMMON_CONSTANTS.KAFKA_CRAWL_TOPIC)
    for message in consumer:
        crawl.delay(message)
