import os
import sys
import django

import pandas as pd
import numpy as np

sys.path.append("/home/palash/Desktop/palash/county-list/backend/country/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "country.settings")
django.setup()


from test_rest.models import CountryDetail

def main():
	# dfr = pd.read_csv('data_analysis/captured_data/country_population.csv')
	# # print(dfr)
	# rows, columns = dfr.shape
	# import pdb
	# pdb.set_trace()

	cdata = CountryDetail.objects.filter(population__isnull=False).values('name', 'population')
	dfr = pd.concat([pd.Series(d) for d in cdata], axis=1).fillna(0).T

	max_five_countries = dfr.sort_values('population', ascending = False)[:5]
	
	print(max_five_countries)
	# print(rows, columns)




if __name__ == '__main__':
	main()