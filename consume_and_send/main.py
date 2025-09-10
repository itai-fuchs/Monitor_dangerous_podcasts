from mongo_dal import MongoDAL
from elastic_dal import EsDAL
import config
from kafka_client import Consumer

from id_generetor import add_content_hash_id
from logger import Logger



logger = Logger.get_logger(__name__)


#Initializes text_analysis consumer object
# & connection to Mongo & create elastic index.

mongo_cli=MongoDAL()
es=EsDAL()
es.create_index()
#Initialize kafka consumer
consumer=Consumer(config.TOPIC, config.KAFKA_BOOTSTRAP).consumer




#Loops over message that the consumer receives.
#Adds an ID. And sends them to Mongo and Elastic respectively.

for message in consumer:
    try:
         #get massage
         doc = message.value

         # add id to massage
         doc=add_content_hash_id(doc)

         #send metaData to elastic
         es.add_document(doc["id"], doc["metaData"])

         # send file to mongo
         mongo_cli.add_document(doc["path"],doc["id"])



    except Exception as e:
      logger.error(f"ERROR: Failed to publish message {message}: {e}")

