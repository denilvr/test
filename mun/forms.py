from .models import Mun
from django import forms 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MunForm(forms.ModelForm):
	empID = forms.CharField(max_length=10, required=True, help_text='Required')
	first_name = forms.CharField(max_length=30, required=True, help_text='Required')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	email = forms.EmailField(max_length=254)

	class Meta:
		model = Mun
		fields = ('empID', 'first_name', 'last_name', 'email')
		