from django.shortcuts import render
from .forms import MunForm
# Create your views here.



def mun_form(request):
    return render(request, 'mun/mun_form.html', {})

def mun_form(request):
	if request.method == 'POST':
		form = MunForm(request.POST)
		if form.is_valid():
			form.save()
			print("hello")
			return render(request, 'mun/mun_home.html', {})
	else:
		form = MunForm()
	return render(request, 'mun/mun_home.html', {
		'form': form
	})