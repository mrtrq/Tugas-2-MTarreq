from multiprocessing import context

from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.

def show_katalog(request):
    return render(request, 'katalog.html', context)

catalog = CatalogItem.objects.all()
context = {
        'list_katalog': catalog,
        'nama': 'Tarreq'
    }

