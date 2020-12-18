from django.shortcuts import render
from .models import Synth

from django.views.generic.edit import CreateView,DeleteView,UpdateView
# Create your views here.
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
    return render(request, 'synths/details.html', {'synth':synth})

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