from kafka import KafkaConsumer
import config
import json, logging


logger = logging.getLogger(__name__)

try:

    consumer = KafkaConsumer(
        config.GET_TOPIC,
        bootstrap_servers=config.KAFKA_BROKERS,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )
    logger.info("KafkaConsumer created successfully")

except Exception as e:
    logger.error(f"Error creating KafkaConsumer: {e}")

