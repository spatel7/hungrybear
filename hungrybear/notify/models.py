from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone = PhoneNumberField()
	preferences = models.CharField(max_length=128)
	verification_num = models.IntegerField(default=0)
	verified = models.BooleanField(default=False)
	def __unicode__(self):
		return self.user.username
