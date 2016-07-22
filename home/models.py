from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bits_id = models.CharField(max_length = 12, blank = False)
	full_name = models.CharField(max_length = 120, blank = False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	email = models.EmailField()
	student_mobile = models.CharField(max_length = 10)

	def __str__(self):
		return self.full_name

	