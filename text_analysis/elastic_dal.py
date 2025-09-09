from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import config

from logger import Logger
logger = Logger.get_logger(__name__)




class EsDAL:

    """
    class to update doc in elastic to add podcast meta data
    """
    def __init__(self, host=config.ELASTIC_HOST, index=config.ELASTIC_INDEX):
        try:
            self.es = Elasticsearch(host)
            logger.info(f"info: connect to Elasticsearch successfully")
        except Exception as e:
            logger.error(f"ERROR: Failed to connect to Elasticsearch: {e}")
            raise
        self.index = index


    def update_file(self, unique_id, val):

        updated_data = {
            val}

        try:
            response = self.es.update(index=self.index, id=unique_id, body={"doc": updated_data})
            logger.info(f"Document updated successfully: {response['result']}")
        except Exception as e:
            logger.error(f"Error updating document: {e}")


    def get_file_stt(self, document_id,field_to_retrieve):
        try:
            # Get the document and specify the _source_includes parameter
            response = self.es.get(
                index=self.index,
                id=document_id,
                _source_includes=[field_to_retrieve]
            )

            if response.get('found'):
                # Access the specific field from the _source
                field_value = response['_source'].get(field_to_retrieve)
                return field_value.lower()
            else:
                print(f"Document with ID '{document_id}' not found in index '{self.index}'.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def get_all_files_id(self):
        s = Search(using=self.es, index=self.index)

        # Exclude the _source field to retrieve only metadata (including _id)
        s = s.source(False)

        # Use scan to efficiently retrieve all document IDs
        document_ids = [hit.meta.id for hit in s.scan()]
        return document_ids

# def get_document(self):
#     response = self.es.search(index=self.index_name, query={"match_all": {}}, size=1000)
#     return response['hits']['hits']
#
#
# es = ElasticDAL()
# for i in es.get_document():
#     print(i["_source"]["stt"])