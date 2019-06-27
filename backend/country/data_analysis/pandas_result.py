import os
import sys
import django

import pandas as pd
import numpy as np

sys.path.append("/home/palash/Desktop/palash/county-list/backend/country/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "country.settings")
django.setup()

from ..test_rest.models import CountryDetail


def countries_insights():
    # dfr = pd.read_csv('data_analysis/captured_data/country_population.csv')
    # rows, columns = dfr.shape
    cdata = CountryDetail.objects.filter(population__isnull=False).values('name', 'population')
    dfr = pd.concat([pd.Series(d) for d in cdata], axis=1).fillna(0).T

    max_five_countries = dfr.sort_values('population', ascending=False)[:5]
    print(max_five_countries)


# print(rows, columns)


def pandas_testing():

# if __name__ == '__main__':
# 	main()
