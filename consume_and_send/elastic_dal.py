from elasticsearch import Elasticsearch
import config

from logger import Logger
logger = Logger.get_logger(__name__)




class EsDAL:

    """
    class to create index in elastic & add podcast meta data
    """
    def __init__(self, host=config.ELASTIC_HOST, index=config.ELASTIC_INDEX):
        try:
            self.es = Elasticsearch(host)
            logger.info(f"info: connect to Elasticsearch successfully")
        except Exception as e:
            logger.error(f"ERROR: Failed to connect to Elasticsearch: {e}")
            raise
        self.index = index

    def create_index(self, mapping=config.ELASTIC_MAPPING):
        try:
            if self.es.indices.exists(index=self.index):
                self.es.indices.delete(index=self.index)


            self.es.indices.create(index=self.index, body={"mappings": mapping})
            logger.info(f"info: create index {self.index} successfully")
        except Exception as e:
            logger.error(f"Error: creating index {self.index}: {e}")


    def add_podcast(self, unique_id, metadata):
        try:
            self.es.index(index=self.index, id=unique_id, document=metadata)
            logger.info(f"info: add podcast {unique_id} successfully to elastic")
        except Exception as e:
            logger.error(f"Error: Failed to add to elastic {unique_id}: {e}")





