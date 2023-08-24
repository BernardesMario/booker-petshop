from pytest_django.asserts import assertTemplateUsed
from reserva.models import EspeciesPet
import pytest
'''
@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    #Arrange
    EspeciesPet(
        especie = 'Outro'
    ).save
    #Act
    response = client.get('/reserva/criar/')
    #Assert
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')
'''

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    # Arrange
    EspeciesPet(
        especie = 'Outro'
    ).save()
    
    # Act
    response = client.get('/reserva/criar/')
    
    # Assert
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')

