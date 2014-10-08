from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PerfilUser(models.Model):
	user=models.OneToOneField(User)

	nick=models.IntegerField()
	email=models.EmailField()
