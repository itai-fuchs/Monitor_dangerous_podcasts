from elasticsearch import Elasticsearch
import logging
import config
logger = logging.getLogger(__name__)




class EsDAL:
    def __init__(self, host=config.ELASTIC_HOST, index=config.ELASTIC_INDEX):
        self.es = Elasticsearch(host)
        self.index = index

    def create_index(self, mapping=config.ELASTIC_MAPPING):

        if self.es.indices.exists(index=self.index):
            self.es.indices.delete(index=self.index)


        self.es.indices.create(index=self.index, body={"mappings": mapping})
        logger.info(self.es.indices.get_mapping(index=self.index))


    def add_podcast(self, unique_id, metadata):
        self.es.index(index=self.index, id=unique_id, document=metadata)




