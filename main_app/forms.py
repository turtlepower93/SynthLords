from django.forms import ModelForm
from .models import Patch

class PatchesForm(ModelForm):
    class Meta:
        model = Patch
        fields = ['name','category','author']