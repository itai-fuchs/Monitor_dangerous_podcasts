import logging
from mongo_dal import MongoDAL
from elastic_dal import EsDAL
import config
from kafka_client import Consumer
from id_generetor import add_content_hash_id


logger = logging.getLogger(__name__)


#Initializes a consumer object & connection to Mongo & an elastic index.

mongo_cli=MongoDAL()
es=EsDAL()
es.create_index()
consumer=Consumer(config.GET_TOPIC,config.KAFKA_BOOTSTRAP).consumer


#Loops over the message that the consumer receives.
# Adds an id to them and sends them to Mongo and Elastic respectively.
try:
   for message in consumer:


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

finally:
   consumer.close()