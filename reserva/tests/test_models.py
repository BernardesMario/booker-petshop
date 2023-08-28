from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva

#FIXTURE

@pytest.fixture
def reserva_today():
    reserva_today = baker.make(
        Reserva,
        nome = 'tom',
        data=date.today(),
        turno='Tarde'
    )
    return reserva_today


@pytest.mark.django_db
def test_reserva_deve_retornar_string_formatada(reserva_today):
    # Arrange
    
    # Act

    # Assert
    assert str(reserva_today) == 'tom: 2023-08-27 - Tarde'

