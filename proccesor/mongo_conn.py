import pymongo
import logging


logger = logging.getLogger(__name__)


class MongoConn:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = pymongo.MongoClient(self.mongo_uri)
                # Ping to check connection
                print(self.conn.admin.command('ping'))

                logging.info("Connected to MongoDB successfully.")
            except Exception as e:
                logging.error(f"MongoDB connection error: {e}")
                self.conn = None
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logging.info("MongoDB connection closed.")
        return None
