from pytest_django.asserts import assertTemplateUsed
from reserva.models import EspeciesPet
import pytest

@pytest.mark.django_db
def teste_view_inicio_template(client):
    # Arrange
    EspeciesPet(
        especie = 'Outro'
    ).save()
    
    #Act
    response = client.get('')

    # Assert
    assert response.status_code == 200
    assertTemplateUsed(response, 'inicio.html')

@pytest.mark.django_db
def teste_view_contato_template(client):
    #Arrange

    #Act
    response = client.get('/contato/')

    #Assert
    assert response.status_code == 200
    assertTemplateUsed(response, 'contato.html')