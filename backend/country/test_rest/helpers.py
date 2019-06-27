import requests
from django.conf import settings
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch

ES = settings.ELASTICSEARCH
HOST = ES['host']
PORT = ES['port']


class ElasticSearchClient:
    """client class for ES"""

    def client(self):
        res = requests.get(ES['protocol'] + '://' + HOST + ':' + str(PORT))
        es = Elasticsearch([{'host': HOST, 'port': PORT}])
        return res, es


    def get_index(self):
        return ES['index']



