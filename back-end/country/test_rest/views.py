from django.shortcuts import render

# Create your views here.


import requests
from bs4 import BeautifulSoup
import json
import re

from country.response import api_response
from rest_framework.views import APIView


headers={"Access-Control-Allow-Credentials":"True"}
content_type='application/json'

class CountryList(APIView):
	"""
	List of all the countries
	"""

	@api_response
	def get(self, request):
		try:
			url = "https://www.britannica.com/topic/list-of-countries-1993160"
			response = requests.get(url)
			soup = BeautifulSoup(response.text)
			scripts = soup.find_all(attrs={'class': re.compile(r"^md-crosslink$")})
			#print(scripts)


			all_countries = []
			for script in scripts:
				content = script.get_text()
				all_countries.append(content)
				
			data = []
			for country in all_countries:
				if country[0].isupper():
					# print(country)
					country_data = {
						'name' : country
					}
					data.append(country_data)

			
			return {"status": 1, "data": data}


		except Exception:
			return {'status': 0, 'message': "No country is available!"}


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


