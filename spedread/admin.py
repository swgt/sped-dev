from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Bloco)
admin.site.register(Registro)

class CampoAdmin(admin.ModelAdmin):
    list_display = ('registro','nome','num_posicao', 'descricao')

admin.site.register(Campo, CampoAdmin)

admin.site.register(Sped)