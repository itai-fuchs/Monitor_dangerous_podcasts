import logging
import config
from kafka_client import producer
from load_files import DirectoryScanner
from metadata_extraction import MetadataExtraction

logger = logging.getLogger(__name__)

files_list=DirectoryScanner(config.FILE_PATH).get_files()

for file in files_list:
   json= MetadataExtraction(file).get_json()
   try:
      producer.send(config.TOPIC,json)
   except Exception as e:
            logger.error(f"Failed to publish document: {e}")

   producer.flush()