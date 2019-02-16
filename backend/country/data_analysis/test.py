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
	cdata = CountryDetail.objects.filter(population__isnull=False).values('name', 'population')
	dfr = pd.concat([pd.Series(d) for d in cdata], axis=1).fillna(0).T

	import pdb
	pdb.set_trace()
	# dfr.to_excel('data_analysis/captured_data/country_population.xlsx')
	dfr.to_csv('data_analysis/captured_data/country_population.csv')
	print(dfr)




if __name__ == '__main__':
	main()