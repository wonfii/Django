from places.models import Place
from django.shortcuts import render

# Create your views here.
def ua_map(request):
    places = Place.objects.all()
    return render(request, 'index.html', {'places': places})

