from kafka import KafkaProducer
import json

from logger import Logger
logger = Logger.get_logger(__name__)

# create kafka producer

class Producer:

    def __init__(self,kafka_bootstrap):
        try:

            self.producer = KafkaProducer(
                bootstrap_servers=kafka_bootstrap,
                value_serializer=lambda x: json.dumps(x).encode("utf-8")

            )
            logger.info("info: KafkaProducer created successfully")

        except Exception as e:
            logger.error(f"Error: creating KafkaProducer: {e}")