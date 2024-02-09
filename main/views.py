from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(req):
    return HttpResponse('<h1>This is Main</h1>')
