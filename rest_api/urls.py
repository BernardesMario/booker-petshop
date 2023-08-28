from django.urls import path
from rest_api.views import ListaEspeciesPetOutros, ListaEspeciesPetCachorro,ListaEspeciesPetGato, PetshopModelViewSet, AgendamentoModelViewSet, AgendamentosHojeModelViewSet, AgendamentosSemanaModelViewSet, EspeciesViewSet
from rest_framework.routers import SimpleRouter

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('hoje', AgendamentosHojeModelViewSet)
router.register('semana', AgendamentosSemanaModelViewSet)
router.register('petshop', PetshopModelViewSet)
router.register('pets', EspeciesViewSet)
router.register('gatos', ListaEspeciesPetGato)
router.register('cachorro', ListaEspeciesPetCachorro)
router.register('outros', ListaEspeciesPetOutros)

urlpatterns = []

urlpatterns += router.urls

