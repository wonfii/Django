from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def about(request):
    return render(request, 'aboutPage.html')

def artworks(request):
    return render(request, 'artworksPage.html')

