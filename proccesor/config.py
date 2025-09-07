import logging
import os

#log config
logging.basicConfig(level=logging.WARNING)




#kafka conf
KAFKA_BROKERS = ["localhost:9092"]

GET_TOPIC="PODCASTS_INFO"

#elastic conf

ELASTIC_CONN ="http://localhost:9200"
INDEX_NAME="podcats_mataData"

CUSTOM_MAPPING = {
    "properties": {
        "PodacastID": {"type": "float"},
        "MeataData": {
            "type": "text",
        }
    }
}

#mongo conf
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_DB   = os.getenv("MONGO_DB", "appdb")
MONGO_USER = os.getenv("MONGO_USER", "appuser")
MONGO_PASS = os.getenv("MONGO_PASS", "apppass")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE", MONGO_DB)

MONGO_URI  = os.getenv(
    "MONGO_URI",
    f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
)

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "podcast")
