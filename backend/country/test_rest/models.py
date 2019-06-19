from django.db import models

# Create your models here.

class CountryDetail(models.Model):
	"""country name description etc"""
	name = models.CharField(max_length=256, unique=True)
	description = models.TextField(max_length=5000, blank=True, null=True)
	capital = models.CharField(max_length=100, blank=True, null=True)
	population = models.IntegerField(verbose_name="Total Population", blank=True, null=True)
	flag = models.CharField(max_length=500, blank=True, null=True)
	currency = models.CharField(max_length=100, blank=True, null=True)
	largest_city = models.CharField(max_length=100, blank=True, null=True)


	def __str__(self):
		return self.name


