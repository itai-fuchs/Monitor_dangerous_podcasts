import logging
logger = logging.getLogger(__name__)


class MongoDAL:
    def __init__(self, conn, db_name, collection_name):
        self.conn = conn
        self.db = self.conn[db_name]
        self.collection_name = collection_name
        self.collection = self.db[collection_name]

    def create_coll(self):
        try:
            if self.collection_name not in self.db.list_collection_names():
                self.db.create_collection(self.collection_name)
                logging.info(f"Collection '{self.collection_name}' created.")
            else:
                logging.info(f"Collection '{self.collection_name}' already exists.")
        except Exception as e:
            logging.error(f"Failed to create collection '{self.collection_name}': {e}")


    def add_doc(self, document):
        try:
            result = self.collection.insert_one(document)
            logging.info(f"Inserted document into '{self.collection_name}': {document}")
            return result.inserted_id
        except Exception as e:
            logging.error(f"Failed to insert into '{self.collection_name}': {e}")
            return None
