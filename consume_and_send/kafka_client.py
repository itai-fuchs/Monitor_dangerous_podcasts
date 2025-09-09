from kafka import KafkaConsumer
import json

from logger import Logger
logger = Logger.get_logger(__name__)

class Consumer:
    """
    class to create consumer object.
    """

    def __init__(self,topic, bootstrap_servers):
        try:

            self.consumer = KafkaConsumer(
                topic,
                bootstrap_servers=bootstrap_servers,
                value_deserializer=lambda x: json.loads(x.decode("utf-8")),
                auto_offset_reset="earliest",
                enable_auto_commit=True
            )
            logger.info("info: KafkaConsumer created successfully")

        except Exception as e:
            logger.error(f"Error: creating KafkaConsumer: {e}")

