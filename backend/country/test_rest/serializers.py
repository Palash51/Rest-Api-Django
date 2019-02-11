from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from test_rest.models import CountryDetail

class CountryDetailSerializer(serializers.ModelSerializer):
	"""country data"""

	class Meta:
		model = CountryDetail
		fields = ("name",)

