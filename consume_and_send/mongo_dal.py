import logging
import config
import gridfs
from pymongo import MongoClient

logger = logging.getLogger(__name__)

class MongoDAL:
    def __init__(self):
        try:
            client = MongoClient(config.MONGO_URI)
            logger.info("Connected to MongoDB successfully")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
        self.db = client[config.MONGO_DB]
        self.collection = self.db[config.MONGO_COLLECTION]
        self.fs = gridfs.GridFS(self.db)

    def add_podcast(self, file_path, unique_id):
        try:
            with open(file_path, "rb") as f:
                file_id = self.fs.put(f, filename=unique_id)
            return str(file_id)
        except Exception as e:
            logger.error(f"Failed to open file: {e}")