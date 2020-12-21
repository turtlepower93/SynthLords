from django.contrib import admin
from .models import Synth, Patch, Artist

# Register your models here.

admin.site.register(Synth)
admin.site.register(Patch)
admin.site.register(Artist)