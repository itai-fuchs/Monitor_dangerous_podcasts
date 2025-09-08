import logging
from mongo_dal import MongoDAL
from elastic import EsDAL
import config
from kafka_client import consumer
import hashlib
import json

logger = logging.getLogger(__name__)


def add_content_hash_id(data, length=10):
   data_str = json.dumps(data, sort_keys=True)
   hash_id = hashlib.sha256(data_str.encode()).hexdigest()[:length]
   data["id"] = hash_id
   return data



mongo_cli=MongoDAL()
es=EsDAL()
es.create_index()


for message in consumer:
   try:

      doc = message.value
      doc=add_content_hash_id(doc)
      try:
         es.add_podcast(doc["id"], doc["metaData"])
      except Exception as e:
         logger.error(f"Failed to send to elastic: {e}")
      try:
         mongo_cli.add_podcast(doc["path"],doc["id"])

      except Exception as e:
         logger.error(f"Failed to send to mongo: {e}")

   except Exception as e:
      logger.error(f"Failed to publish document: {e}")
