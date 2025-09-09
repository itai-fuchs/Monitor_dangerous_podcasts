import os




FILES_PATH="C:/podcasts"

#kafka conf
KAFKA_BOOTSTRAP = ["localhost:9092"]

TOPIC="PODCASTS_INFO"



#elastic conf

ELASTIC_HOST ="http://localhost:9200"
ELASTIC_INDEX="podcats"
ELASTIC_MAPPING ={
    "properties": {
      "path": {
        "type": "keyword"
      },
      "metaData": {
        "properties": {
          "File_name": {
            "type": "keyword"
          },
          "File_stem": {
            "type": "keyword"
          },
          "File_suffix": {
            "type": "keyword"
          },
          "Creation_Time": {
            "type":"keyword"

          },
          "Last_Modified": {
            "type":"keyword"

          },
          "Last_Accessed": {
            "type": "keyword"

          },
          "file_size_bytes": {
            "type": "long"
          },
          "file_size_mb": {
            "type": "float"
          }
        }
      }
    }
  }



#mongo conf
# MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
# MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
MONGO_DB   = os.getenv("MONGO_DB", "IDF")
# MONGO_USER = os.getenv("MONGO_USER", "localhost")
# MONGO_PASS = os.getenv("MONGO_PASS", "apppass")

MONGO_URI ="mongodb://localhost:27017/"
# MONGO_URI  = os.getenv(
#     "MONGO_URI",
#     f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
# )

MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "podcasts_files")










