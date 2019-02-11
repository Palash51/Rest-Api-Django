from bs4 import BeautifulSoup
import json
import re
import requests

from django.core.management.base import BaseCommand
from django.utils import timezone
from test_rest.models import CountryDetail

class Command(BaseCommand):
    help = 'Fetch all countries name'

    def handle(self, *args, **kwargs):
    	url = "https://www.britannica.com/topic/list-of-countries-1993160"
    	response = requests.get(url)
    	soup = BeautifulSoup(response.text)
    	scripts = soup.find_all(attrs={'class': re.compile(r"^md-crosslink$")})
    	all_countries = []
    	for script in scripts:
    		content = script.get_text()
    		all_countries.append(content)

    	data = []
    	for country in all_countries:
    		if country[0].isupper():
    			try:
    				new_country = CountryDetail.objects.get(name=country)
    			except Exception:
    				new_country = CountryDetail.objects.create(name=country)

    	self.stdout.write("All countries are added")				

        