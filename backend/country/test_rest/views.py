import requests
from bs4 import BeautifulSoup
import json
import re
from django.shortcuts import render
from country.response import api_response
from rest_framework.views import APIView
from rest_framework import generics
from test_rest.models import CountryDetail
from test_rest.serializers import CountryDetailSerializer, CountryDataSerializer
from test_rest.wiki_scripts import get_country_details

headers={"Access-Control-Allow-Credentials":"True"}
content_type='application/json'


class CountryList(APIView):
	"""
	List of all the countries
	"""

	@api_response
	def get(self, request):
		try:
			all_countries = CountryDetail.objects.all()
			all_countries_serializer = CountryDetailSerializer(all_countries, many=True).data
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


