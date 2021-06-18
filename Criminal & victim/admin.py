from django.contrib import admin
from .models import Criminal, FIR, Victim, Writer

# Register your models here.

admin.site.register(Writer)
admin.site.register(Criminal)
admin.site.register(Victim)
admin.site.register(FIR)