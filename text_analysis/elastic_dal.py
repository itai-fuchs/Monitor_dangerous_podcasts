from elasticsearch import Elasticsearch

from elasticsearch import helpers
import config

from logger import Logger
logger = Logger.get_logger(__name__)



class EsDAL:

    """
    class to add new fild to doc in elastic.
    """
    def __init__(self, host=config.ELASTIC_HOST, index=config.ELASTIC_INDEX):
        try:
            self.es = Elasticsearch(host)
            logger.info(f"info: connect to Elasticsearch successfully")
        except Exception as e:
            logger.error(f"ERROR: Failed to connect to Elasticsearch: {e}")
            raise
        self.index = index


    def update_document_filed(self, unique_id, val):
        try:
            response = self.es.update(index=self.index, id=unique_id, body={"doc": val})
            logger.info(f"info: Document  updated successfully")
        except Exception as e:
            logger.error(f"Error: updating document : {e}")


    def get_documents_filed(self,field_to_retrieve):
        """

      For each document, returns its id and a given field.
        """
        try:
            hits = helpers.scan(
                self.es,
                query={"query": {"match_all": {}}},
                scroll='1m',
                index=self.index
            )
            doc=[]
            for hit in hits:
                if field_to_retrieve in hit["_source"]:
                    doc.append([hit['_id'],hit["_source"][field_to_retrieve]])
                    logger.info(f"info: get stt from {hit['_id']} successfully")
                else: logger.info(f"warning: {hit['_id']} dont have stt filed")
            return doc
        except Exception as e:
            logger.error(f"error: failed to get all document id {e}")



