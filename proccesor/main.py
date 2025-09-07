import logging
from mongo_dal import MongoDAL
from mongo_conn import MongoConn
# from elastic import Elastic
import config
# from kafka_client import consumer
import uuid


logger = logging.getLogger(__name__)

doc ={"name":"itai"}
conn=MongoConn(config.MONGO_URI)
conn.connect()
print(conn.conn)

mongo=MongoDAL(conn.conn,config.MONGO_DB,config.MONGO_COLLECTION)

mongo.add_doc(doc)



# es=Elastic(config.ELASTIC_CONN,config.INDEX_NAME,config.CUSTOM_MAPPING)
#
# es.create_index()


def addID(json):
   json["id"] = str(uuid.uuid4())




# for message in consumer:
#    try:
#       topic = message.topic
#       doc = message.value
#       addID(doc)
#       pprint(doc)
#
#
#    except Exception as e:
#       logger.error(f"Failed to publish document: {e}")
#
#
#


