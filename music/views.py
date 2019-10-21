from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Music homepage")
# Create your views here.
