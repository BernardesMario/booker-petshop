'''def test_config():
    assert 1 == 1
'''

from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva

#FIXTURE
@pytest.fixture
def reserva():
    reserva = baker.make(
        Reserva,
        nome = 'tom',
        data=date.today(),
        turno='Tarde'
    )
    return reserva

@pytest.mark.django_db
def test_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'tom: 2023-08-23 - Tarde'