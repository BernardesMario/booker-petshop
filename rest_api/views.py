from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from reserva.models import Reserva, Petshop, EspeciesPet
from rest_api.serializers import ListaEspeciePetSerializer, AgendamentoModelSerializer, PetshopModelSerializer, EspeciesModelSerializer, EspeciesPetSerializer
from datetime import date, timedelta

# Create your views here.
class AgendamentoModelViewSet(ModelViewSet):
   queryset = Reserva.objects.all()
   serializer_class = AgendamentoModelSerializer
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]

class AgendamentosHojeModelViewSet(ModelViewSet):
    hoje = date.today()
    queryset = Reserva.objects.filter(data = hoje)
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AgendamentosSemanaModelViewSet(ModelViewSet):
    data_atual = date.today()
    data_semana_passada = data_atual - timedelta(days=7)
    registro = Reserva.objects.filter(data__gte=data_semana_passada, data__lte=data_atual)
    queryset = registro
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class EspeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EspeciesPet.objects.all()
    serializer_class = EspeciesPetSerializer
    filterset_fields = ['especie']

@api_view(['GET','POST']) #metodo GET e POST acessam API
def hello_world(request):
    if request.method == 'POST':
        return Response({'mensagem': f'Hello, {request.data.get("Name")}'})
    return Response({'hello': 'world API'})

class ListaEspeciesPetGato(ReadOnlyModelViewSet):
    especie_alvo = EspeciesPet.objects.filter(especie='Gato').first()
    queryset = Reserva.objects.filter(especie=especie_alvo)
    serializer_class = ListaEspeciePetSerializer
class ListaEspeciesPetCachorro(ReadOnlyModelViewSet):
#especie_alvo = EspeciesPet.objects.get(tipo='Cachorro')
    queryset = Reserva.objects.filter(especie__especie='Cachorro')
    serializer_class = ListaEspeciePetSerializer
class ListaEspeciesPetOutros(ReadOnlyModelViewSet):
    especie_alvo = EspeciesPet.objects.get(especie='Outro')
    queryset = Reserva.objects.filter(especie=especie_alvo)
    serializer_class = ListaEspeciePetSerializer
#Agendamento.objects.filter(especie__especie=variavel)
