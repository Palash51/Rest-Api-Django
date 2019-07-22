import pandas as pd
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

from captured_data.constant import country_data

connections.create_connection(hosts=['localhost'])


def main():
    """
    creating index using
     1)django models
     2)csv/json file
    :return:
    """
    res = requests.get('http://localhost:9200')
    # print(res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    # country_data = list(CountryDetail.objects.values('id', 'name', 'description', 'capital', 'population', 'largest_city'))
    # print(len(country_data))

    # with open('/home/palash/Desktop/palash/country-dataset/data.json', 'r') as json_file:
    #     import pdb
    #     pdb.set_trace()
    #     data = json.load(json_file)


    final_data = country_data

    for country in final_data:
        es.index(index='all_countries', doc_type='all_country', body=json.dumps(country))





    print("Done!!!")


if __name__ == '__main__':
    main()
