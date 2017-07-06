from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(request):
    entries = Entry.objects.all()
    return render( request, 'entries/index.html', {'entries':entries} )
