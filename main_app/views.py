from django.shortcuts import render, redirect
from .models import Synth
from .forms import PatchesForm

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
    patches_form = PatchesForm()
    return render(request, 'synths/details.html', {
        'synth':synth,
        'patches_form' : patches_form})

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

def add_patch(request, synth_id):
    print('Hi')
    form = PatchesForm(request.POST)
    if form.is_valid():
        new_patch = form.save(commit=False)
        new_patch.synth_id = synth_id
        new_patch.save()
    return redirect('details', synth_id=synth_id)
