from django.db import models

# Create your models here.


class Mun(models.Model):    
	empID = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.empID