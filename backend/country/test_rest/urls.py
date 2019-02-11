from django.contrib import admin
from django.urls import path

from test_rest.views import CountryList

app_name = 'test_rest'

urlpatterns = [
    path('contries/v1/', CountryList.as_view() , name='country_list')]
