import pytest
import datetime
from model_bakery import baker
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

#Verificar se o serializer AgendamentoModelSerializer é capaz de 
#idenficicar dados invalidos e falhar na validação corretamente
@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today()- datetime.timedelta(days=1)
    petshop = baker.make(Petshop)
    return {
        'nome' : 'nome_teste',
        'email': 'email@test.com',
        'nome_pet': 'test_pet',
        'data': ontem,
        'turno': 'Tarde',
        'tamanho': 0,
        'observacoes': '.',
        'petshop':petshop.pk
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()