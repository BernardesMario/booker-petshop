import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_todos_petshops():
    # Arrange
    cliente = APIClient()
    
    # Act
    resposta = cliente.get('/api/petshop')
    
    #Assert
    assert resposta.data['count'] == 0
