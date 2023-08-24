from django.contrib import admin
from reserva.models import Reserva
# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data']
    search_fields = ['nome_pet']
    list_filter = ['data', 'turno', 'tamanho']