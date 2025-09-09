import gridfs
from pymongo import MongoClient
from logger import Logger

import config
logger = Logger.get_logger(__name__)

class MongoDAL:
    """
    Class for connecting with mongo to get files using the gridfs library
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



    def get_file_by_id(self,id):
        try:
            file = self.fs.find_one({'filename': id})
            logger.info(f"get file {id} from MongoDB successfully")
            return file
        except Exception as e:
            logger.error(f"ERROR: Failed to get file {id} from MongoDB: {e}")


    def get__all_files_id(self):
            return [f.filename for f in self.fs.find({})]





