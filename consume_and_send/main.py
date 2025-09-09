from mongo_dal import MongoDAL
from elastic_dal import EsDAL
import config
from kafka_client import Consumer
from STT import AudioTranscriber
from id_generetor import add_content_hash_id
from logger import Logger



logger = Logger.get_logger(__name__)


#Initializes a consumer object & connection to Mongo & an elastic index.

mongo_cli=MongoDAL()
es=EsDAL()
es.create_index()
consumer=Consumer(config.TOPIC, config.KAFKA_BOOTSTRAP).consumer
audio_transcriber=AudioTranscriber()


#Loops over a message that the consumer receives.
#Adds an ID and a transcript to them. And sends them to Mongo and Elastic respectively.

for message in consumer:
    try:
         #get massage
         doc = message.value

         # add id to massage
         doc=add_content_hash_id(doc)

         # add STT to metadata
         text = audio_transcriber.transcribe(doc["path"])
         doc["metaData"]["stt"]=text

         #send metaData to elastic
         es.add_podcast(doc["id"], doc["metaData"])

         # send file to mongo
         mongo_cli.add_podcast(doc["path"],doc["id"])



    except Exception as e:
      logger.error(f"ERROR: Failed to publish message {message}: {e}")

