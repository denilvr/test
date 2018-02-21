from django.shortcuts import render

# Create your views here.



def mun_form(request):
    return render(request, 'mun/mun_form.html', {})