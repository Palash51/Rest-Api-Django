from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch

import os
import sys
import django
import requests
import json



sys.path.append("/home/palash/Desktop/palash/county-list/backend/country/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "country.settings")
django.setup()

from test_rest.models import CountryDetail
from test_rest.helpers import ElasticSearchClient

connections.create_connection(hosts=['localhost'])


def main():
    res = requests.get('http://localhost:9200')
    # print(res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    country_data = list(CountryDetail.objects.values('id', 'name', 'description', 'capital', 'population', 'largest_city'))
    print(len(country_data))

    for country in country_data:
        es.index(index='country', doc_type='country',id=country['id'], body=json.dumps(country))



if __name__ == '__main__':
    main()
