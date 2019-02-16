import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import urllib.request
from urllib.request import urlopen

import wikipedia
from lxml import etree

def get_country_details(country_name):
	"""fetch countries data"""
	# if not re.match(r'^\w+$', country_name):
	# 	return False
	new_url = "http://dbpedia.org/page/" + country_name.capitalize().replace(" ", "_")

	resp = urllib.request.urlopen(new_url)
	soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

	table = soup.find('table', class_='description table table-striped')

	result = {}
	result['description'] = soup.find('p', attrs={'class' : 'lead'}).text
	for tr in table.find_all('tr'):
		if len(tr.find_all('td')) == 2:

			if 'capital' in tr.find_all('td')[0].text.strip("dbo:").strip("\n") and 'capital' not in result.keys():
				result['capital'] =  tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_", " ")

			if  'largest city' not in result.keys() and 'largestCity' in tr.find_all('td')[0].text:
				result['largest city'] =  tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_", " ")

			if 'currency' in tr.find_all('td')[0].text.strip("dbo:").strip("\n") and 'currency' not in result.keys():
				result['currency'] =  tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_", " ")

			if 'Total population' not in result.keys() and 'populationTotal' in tr.find_all('td')[0].text.strip("dbo:").strip("\n"):
				result['Total population'] = tr.find_all('td')[1].text.strip("\n").rstrip(" (xsd:integer)")

			if 'flag' not in result.keys() and 'thumbnail' in tr.find_all('td')[0].text.strip("dbo:").strip("\n"):
				result['flag'] = tr.find_all('td')[1].a['href']




	return result


	# wiki_url = "https://en.wikipedia.org/wiki/" + country_name

	# resp = urllib.request.urlopen(wiki_url)
	# soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))


	# req = requests.get(wiki_url)
	# store = etree.fromstring(req.text) 
	# output = store.xpath('//table[@class="infobox vcard"]/tr[th/text()="Motto"]/td/i')

	# site= "http://en.wikipedia.org/wiki/Aldi"
	# import pdb
	# pdb.set_trace()
	# hdr = {'User-Agent': 'Mozilla/5.0'}
	# req = urllib.request.Request(wiki_url,headers=hdr)
	# page = urllib.request.urlopen(req)
	# soup = BeautifulSoup(page.read())
	# table = soup.find('table', class_='infobox geography vcard')
	# result = {}
	# exceptional_row_count = 0


	# json_file = https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=india&rvsection=0
	
	# for tr in table.find_all('tr'):
	# 	import pdb
	# 	pdb.set_trace()
	# 	if tr.find('th'):
	# 		for i in tr.find('th').contents:
	# 			try:
	# 				if "country-name" in i['class']:
	# 					result['country-name'] = i.text
	# 			except Exception:
	# 				pass

	# 	else:
	# 		exceptional_row_count += 1

	# 	if exceptional_row_count > 1:
	# 		print('WARNING ExceptionalRow>1: ', table)
	# print(result)

	# result['name'] = tr.find('th').contents[0].text

	# result[tr.find('th').text] = tr.find('td').text