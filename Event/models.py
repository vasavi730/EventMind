from django.db import models
from django.conf import settings
import uuid
# Create your models here.


class SuperUser(models.Model):
	uname = models.CharField(max_length=40)
	upass = models.CharField(max_length=20)


class DashBoard(models.Model):
	client_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	client_name = models.CharField(max_length=20)
	client_email = models.CharField(max_length=30)
	client_mobile = models.CharField(max_length=10)
	client_address = models.CharField(max_length=50)
	client_event = models.CharField(max_length=20)
	client_status = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class queries(models.Model):
	name = models.CharField(max_length=30)
	email  = models.CharField(max_length=40)
	query = models.CharField(max_length=100)

	def __str__(self):
		return self.name