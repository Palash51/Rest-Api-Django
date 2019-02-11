from django.db import models

# Create your models here.

class CountryDetail(models.Model):
	"""country name description etc"""
	name = models.CharField(max_length=256, unique=True)
	description = models.TextField(max_length=2500, blank=True, null=True)


	def __str__(self):
		return self.name