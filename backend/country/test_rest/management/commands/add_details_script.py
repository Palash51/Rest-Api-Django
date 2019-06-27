import requests
from bs4 import BeautifulSoup, SoupStrainer
import json
import re
import urllib.request
from urllib.request import urlopen

import wikipedia
from lxml import etree
import urllib.request
from django.core.management.base import BaseCommand
from django.utils import timezone
from test_rest.models import CountryDetail


class Command(BaseCommand):
    help = 'Add all countries data'

    def handle(self, *args, **kwargs):
        all_countries = CountryDetail.objects.all()
        for country in all_countries:
            country_name = country.name
            try:

                new_url = "http://dbpedia.org/page/" + country_name.capitalize().replace(" ", "_")

                resp = urllib.request.urlopen(new_url)
                soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
                table = soup.find('table', class_='description table table-striped')

                result = {}
                result['description'] = soup.find('p', attrs={'class': 'lead'}).text
                country.description = result['description']
                for tr in table.find_all('tr'):
                    if len(tr.find_all('td')) == 2:

                        if 'capital' in tr.find_all('td')[0].text.strip("dbo:").strip(
                                "\n") and 'capital' not in result.keys():
                            result['capital'] = tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_", " ")
                            country.capital = result['capital']

                        if 'largest city' not in result.keys() and 'largestCity' in tr.find_all('td')[0].text:
                            result['largest city'] = tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_",
                                                                                                                  " ")
                            country.largest_city = result['largest city']

                        if 'currency' in tr.find_all('td')[0].text.strip("dbo:").strip(
                                "\n") and 'currency' not in result.keys():
                            result['currency'] = tr.find_all('td')[1].text.strip("\n").lstrip("dbr:").replace("_", " ")
                            country.currency = result['currency']

                        # or 'populationCensus'
                        if 'Total population' not in result.keys() and 'populationTotal' in tr.find_all('td')[
                            0].text.strip("dbo:").strip("\n"):
                            result['Total population'] = tr.find_all('td')[1].text.strip("\n").rstrip(" (xsd:integer)")
                            country.population = result['Total population']

                        if 'flag' not in result.keys() and 'thumbnail' in tr.find_all('td')[0].text.strip("dbo:").strip(
                                "\n"):
                            result['flag'] = tr.find_all('td')[1].a['href']
                            country.flag = result['flag']

                country.save()

            except Exception:
                print(country_name)
                pass

        self.stdout.write("All countries data has been added")
