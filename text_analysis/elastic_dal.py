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


    def update_document(self, unique_id, val):
        try:
            response = self.es.update(index=self.index, id=unique_id, body={"doc": val})
            logger.info(f"info: Document  updated successfully: {response['result']}")
        except Exception as e:
            logger.error(f"Error: updating document : {e}")


    def get_document_filed(self, document_id,field_to_retrieve):
        try:
            # Get the document and specify the _source_includes parameter
            response = self.es.get(
                index=self.index,
                id=document_id,
                _source_includes=[field_to_retrieve]
            )

            if response.get('found'):
                # Access the specific field from the _source
                field_value = response['_source'].get(field_to_retrieve).lower()
                logger.info(f"info: get {field_to_retrieve} successfully from Document  ID '{document_id}'")
                return field_value
            else:
                logger.error(f"error: Document with ID '{document_id}' not found in index '{self.index}'.")

        except Exception as e:
            logger.error(f"error: occurred for Document ID {document_id} : {e}")

    def get_all_document_ids(self):
        try:
            hits = helpers.scan(
                self.es,
                query={"query": {"match_all": {}}},
                scroll='1m',
                index=self.index
            )

            ids = [hit['_id'] for hit in hits]
            logger.info(f"info: get all IDS successfully")
            return ids
        except Exception as e:
            logger.error(f"error: failed to get all document id {e}")




