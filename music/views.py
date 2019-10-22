from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def index(request):
    html=' '
    all_albums=Album.objects.all()
    for album in all_albums:
        url='/music/'+str(album.id)+'/'
        html=html+'<a href="' +url+ '">'+album.album_title+'</a><br>'
    return HttpResponse(html)

def details(request ,album_id):
    return HttpResponse("Album Request=>" + str(album_id) )
# Create your views here.
