from django.contrib import admin

# Register your models here.
from data.models import *
admin.site.register(GeneData)
admin.site.register(Mitochondria)
admin.site.register(Microtubule)
admin.site.register(Cell)
