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
        return ES['index'], ES['new_index']


def get_unique_cache_key(request):
    """
        :param request:
        :return: Cache key based on user id and api url which will be unique key in cache
        """

    if request.user.is_anonymous:
        user = 'anonymous'
    else:
        user = request.user.id

    q = getattr(request, request.method)
    q.lists()
    urlencode = q.urlencode(safe='()')

    CACHE_KEY = 'view_cache_%s_%s_%s' % (request.path, user, urlencode)
    return CACHE_KEY
