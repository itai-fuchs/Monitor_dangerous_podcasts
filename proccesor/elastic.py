from elasticsearch import Elasticsearch
import logging


logger = logging.getLogger(__name__)

class Elastic:

    def __init__(self,conn,index_name,mapping):
        self.es = Elasticsearch(conn)

        self.mapp = mapping

        self.index_name = index_name


    def create_index(self):

        if self.es.indices.exists(index=self.index_name):

            self.es.indices.delete(index=self.index_name)

        self.es.indices.create(index=self.index_name, body={"mappings": self.mapp})
        logger.info(self.es.indices.get_mapping(index=self.index_name))

    def add_data(self,data):
        for i, record in enumerate(data):
            self.es.index(index=self.index_name, document=record)
