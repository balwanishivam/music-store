from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Album,Song
from django.template import loader

def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={'all_albums':all_albums,}
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)

#def details(request ,album_id):
    #return HttpResponse("Album Request=>" + str(album_id) )

#raising a Http404 Error
def details(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    '''try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")'''
    return render(request,"music/details.html",{'album':album})
# Create your views here.
