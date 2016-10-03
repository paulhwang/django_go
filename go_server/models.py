from django.db import models

# Create your models here.

class AccountObject(models.Model):
	account = models.CharField(max_length = 32)
	password = models.CharField(max_length = 32)
	name = models.TextField()
