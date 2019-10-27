from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader

def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={
        'all_albums':all_albums,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)

def details(request ,album_id):
    return HttpResponse("Album Request=>" + str(album_id) )
# Create your views here.
