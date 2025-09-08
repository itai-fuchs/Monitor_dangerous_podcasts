import config
from kafka_client import Producer
from load_files import DirectoryScanner
from metadata_extraction import MetadataExtraction
from logger import Logger

logger = Logger.get_logger(__name__)
producer=Producer(config.KAFKA_BOOTSTRAP).producer
files_list = DirectoryScanner(config.FILE_PATH).get_files()

for file in files_list:
    doc = MetadataExtraction(file).get_json()
    try:
        producer.send(config.TOPIC, doc)
        logger.info(f"info: Published document {doc["path"]} successfully")

    except Exception as e:
        logger.error(f"ERROR: Failed to publish document {file}: {e}")

producer.flush()
