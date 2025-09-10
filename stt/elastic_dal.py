from elasticsearch import Elasticsearch
import config

from logger import Logger
logger = Logger.get_logger(__name__)




class EsDAL:


    def __init__(self, host=config.ELASTIC_HOST, index=config.ELASTIC_INDEX):
        try:
            self.es = Elasticsearch(host)
            logger.info(f"info: connect to Elasticsearch successfully")
        except Exception as e:
            logger.error(f"ERROR: Failed to connect to Elasticsearch: {e}")
            raise
        self.index = index


    def update_document(self, unique_id, text):
        """
            method to add stt to doc in elastic
        """

        updated_data = {
            "stt":text}

        try:
            response = self.es.update(index=self.index, id=unique_id, body={"doc": updated_data})
            logger.info(f"info: Document STT updated successfully:")
        except Exception as e:
            logger.error(f"Error: updating document STT: {e}")




