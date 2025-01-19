from places.forms import PlaceForm
from places.models import Place
from django.shortcuts import get_object_or_404, redirect, render

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

def delete(request, name):
    place = get_object_or_404(Place, name=name)
    place.delete()
    return redirect('/')

def edit(request, name):
    place = get_object_or_404(Place, name=name)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('/')  
    else:
        form = PlaceForm(instance=place)
        return render(request, 'edit.html', {'form': form})
    
    return render(request, 'edit.html', {'form': form})