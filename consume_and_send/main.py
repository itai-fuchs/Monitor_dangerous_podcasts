from mongo_dal import MongoDAL
from elastic_dal import EsDAL
import config
from kafka_client import Consumer

from id_generetor import add_content_hash_id
from logger import Logger



logger = Logger.get_logger(__name__)


#Initializes a consumer object & connection to Mongo & an elastic index.

mongo_cli=MongoDAL()
es=EsDAL()
es.create_index()
consumer=Consumer(config.TOPIC, config.KAFKA_BOOTSTRAP).consumer


#Loops over the message that the consumer receives.
# Adds an id to them and sends them to Mongo and Elastic respectively.

for message in consumer:
    try:
         doc = message.value
         doc=add_content_hash_id(doc)
         es.add_podcast(doc["id"], doc["metaData"])
         mongo_cli.add_podcast(doc["path"],doc["id"])


    except Exception as e:
      logger.error(f"ERROR: Failed to publish message {message}: {e}")

