import gridfs
from pymongo import MongoClient
from logger import Logger

import config
logger = Logger.get_logger(__name__)

class MongoDAL:
    """
    Class for connecting with mongo and uploading files using the gridfs library
    """
    def __init__(self):
        try:
            client = MongoClient(config.MONGO_URI)
            logger.info("info: Connected to MongoDB successfully")
        except Exception as e:
            logger.error(f"ERROR: Failed to connect to MongoDB: {e}")
            raise
        self.db = client[config.MONGO_DB]
        self.collection = self.db[config.MONGO_COLLECTION]
        self.fs = gridfs.GridFS(self.db)

    def add_podcast(self, file_path, unique_id):
        try:
            with open(file_path, "rb") as f:
                file_id = self.fs.put(f, filename=unique_id)
            logger.info(f"info: add podcast {file_path} successfully to mongo")
            return str(file_id)
        except Exception as e:
            logger.error(f"ERROR: Failed to add file {file_path} to mongo: {e}")