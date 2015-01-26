from django import forms
from notify.models import UserProfile

class phoneForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("phone",)
