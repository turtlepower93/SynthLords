from django.shortcuts import render, redirect
from .models import Synth, Artist
from .forms import PatchesForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def synths_index(request):
    synths = Synth.objects.all()
    return render(request, 'synths/index.html', {'synths': synths})

def synth_details(request, synth_id):
    synth = Synth.objects.get(id = synth_id)
    patches_form = PatchesForm()
    artists_that_dont_have_synth = Artist.objects.exclude(id__in = synth.artists.all().values_list('id'))
    return render(request, 'synths/details.html', {
        'synth':synth,
        'patches_form' : patches_form,
        'artists': artists_that_dont_have_synth})

def artists_index(request):
    artist = Artist.objects.all()
    return render(request, 'artist/index.html')

def assoc_artist(request, synth_id, artist_id):
    synth = Synth.objects.get(id=synth_id).artists.add(artist_id)
    return redirect('details', synth_id=synth_id)

def disassoc_artist(request,synth_id,artist_id):
    synth = Synth.objects.get(id=synth_id).artists.remove(artist_id)
    return redirect('details', synth_id=synth_id)

class SynthCreate(CreateView):
    model = Synth
    fields = "__all__"
    success_url = '/synths/'

class SynthDelete(DeleteView):
    model = Synth
    success_url = '/synths/'

class SynthUpdate(UpdateView):
    model = Synth
    fields = '__all__'

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistCreate(CreateView):
    model = Artist
    fields ="__all__"

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name','genre']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artists/'

def add_patch(request, synth_id):
    print('Hi')
    form = PatchesForm(request.POST)
    if form.is_valid():
        new_patch = form.save(commit=False)
        new_patch.synth_id = synth_id
        new_patch.save()
    return redirect('details', synth_id=synth_id)
