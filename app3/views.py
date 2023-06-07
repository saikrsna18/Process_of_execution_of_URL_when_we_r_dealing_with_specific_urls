from django.shortcuts import render
from django.http import HttpResponse

def third(request):
    return HttpResponse('my third view')

# Create your views here.
