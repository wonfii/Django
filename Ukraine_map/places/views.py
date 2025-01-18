from places.forms import PlaceForm
from places.models import Place
from django.shortcuts import redirect, render

# Create your views here.
def ua_map(request):
    places = Place.objects.all()
    return render(request, 'index.html', {'places': places})

def create(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('/')  
    else:
        form = PlaceForm()
        return render(request, 'create.html', {'form': form})
    
    return render(request, 'create.html', {'form': form})