from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': 'Socialism is the best economic system!'}

    return render(request,'rango/index.html',context=context_dict)

def about(request):
    return render(request,'rango/about.html')