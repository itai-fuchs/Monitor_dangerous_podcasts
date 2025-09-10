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
