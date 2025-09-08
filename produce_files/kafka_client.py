from kafka import KafkaProducer
import config
import json, logging

# create kafka producer

logger = logging.getLogger(__name__)

try:

    producer = KafkaProducer(
        bootstrap_servers=config.KAFKA_BOOTSTRAP,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")

    )
    logger.info("KafkaProducer created successfully")

except Exception as e:
    logger.error(f"Error creating KafkaProducer: {e}")