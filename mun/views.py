from django.shortcuts import render
from .forms import MunForm
# Create your views here.
from django.contrib import messages
from  django.http import  HttpRequest
from  django.http import  HttpResponseRedirect

def mun_form(request):
	if request.method == 'POST':
		form = MunForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Form Submission Successful.')
			form.save()
			print("hello")
			return HttpResponseRedirect('/')
		else:
			messages.error(request, 'Cannot Submit the Form. Please rectify the Errors.',extra_tags='danger')
	else:
		form = MunForm()
	return render(request, 'mun/mun_home.html', {
		'form': form
	})