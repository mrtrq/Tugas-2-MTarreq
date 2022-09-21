from multiprocessing import context
import re
from django.shortcuts import render
from mywatchlist.models import MovieList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    movies = MovieList.objects.all()
    context = {
    'movies_list' : movies,
    'nama' : 'Tarreq',
    }

    return render(request,"mywatchlist.html", context)

def show_mywatchlist_xml(request):
     movies = MovieList.objects.all()
     return HttpResponse(serializers.serialize("xml", movies), content_type='application/xml')
# Create your views here.

def show_mywatchlist_json(request):
     movies = MovieList.objects.all()
     return HttpResponse(serializers.serialize("json", movies), content_type='application/json')