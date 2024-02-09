from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user(req):
    return HttpResponse('Users Page')
