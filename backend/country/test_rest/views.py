import redis
import requests
from bs4 import BeautifulSoup
import json
import re
from django_redis import get_redis_connection
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.shortcuts import render
from country.response import api_response
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from rest_framework import generics
from test_rest.models import CountryDetail
from test_rest.serializers import CountryDetailSerializer, CountryDataSerializer
from test_rest.wiki_scripts import get_country_details

from .helpers import ElasticSearchClient, get_unique_cache_key

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
r = redis.StrictRedis(host='localhost', port=6379, db=1)
con = get_redis_connection("default")

headers = {
    'Access-Control-Allow-Credentials': 'True',
    'content-type': 'application/json'
}
content_type = 'application/json'


class CountryList(APIView):
    """
    List of all the countries
    """

    @api_response
    def get(self, request):
        # http://127.0.0.1:8001/contries/v1/
        try:
            CACHE_KEY = get_unique_cache_key(self.request)

            if str(CACHE_KEY) in str(r.keys('*')):
                data = r.get(str(CACHE_KEY))
                # data = cache.get(CACHE_KEY)
                return {"status": 1, "data": data}
            all_countries = CountryDetail.objects.all()
            all_countries_serializer = CountryDetailSerializer(all_countries, many=True).data
            # cache.set(CACHE_KEY, all_countries_serializer, timeout=CACHE_TTL)
            r.set(CACHE_KEY, all_countries_serializer)
            return {"status": 1, "data": all_countries_serializer}

        except Exception:
            return {'status': 0, 'message': "No country is available!"}


class CountryDetailView(generics.ListAPIView):
    """details of a country"""

    @api_response
    def post(self, request):
        """get country name and fetch its details"""
        country_name = request.data.get('country_name')
        # country_data = get_country_details(country_name)

        country_data = CountryDetail.objects.get(name__icontains=country_name)
        country_data_serializer = CountryDataSerializer(country_data).data

        if not country_data:
            return {'status': 0, 'message': "Incorrect Country name"}

        return {"status": 1, "data": country_data_serializer}


class SearchCountryES(APIView):
    """Search country details using elastic search"""

    @api_response
    def post(self, request):
        """"""
        try:
            es = Elasticsearch()
            ESC = ElasticSearchClient()
            es_client = ESC.client()
            index_name = ESC.get_index()[1]
            search_url = es_client[0].url + index_name + '*/_search'

            filter_query = es.search(index=index_name, body=request.body)
            if  filter_query['_shards']['successful']:
                return {"status": 1, "data": filter_query}

            return {"status": 0, "data": "errors"}

        except Exception:
            return {"status": 0, "data": "Error in fetching data"}














































# count = 0

# all_countries_dict = {}

# for i in all_countries:

# 	alphabet = i[0]
# 	if alphabet.isupper():
# 		if alphabet not in all_countries_dict.keys():
# 			c_lst = [i]
# 			all_countries_dict[alphabet] = c_lst
# 		else:
# 			c_lst.append(i)


# # print(len(all_countries_dict))

# # print(all_countries_dict)
# # print(sorted(all_countries_dict.keys(), key=lambda x:x.lower()))


# length_dict = {key: len(value) for key, value in all_countries_dict.items()}

# conection_result = {}
# for key in (all_countries_dict.keys() | length_dict.keys()):
# 	if key in all_countries_dict: conection_result.setdefault(key, []).append(all_countries_dict[key])
# 	if key in length_dict: conection_result.setdefault(key, []).append(length_dict[key])


# 	# print(sorted(conection_result.items()))
