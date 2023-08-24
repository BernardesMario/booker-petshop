from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField, ValidationError
from reserva.models import Reserva, Petshop, EspeciesPet
from rest_framework import serializers
import datetime

class EspeciesPetSerializer(ModelSerializer):
    class Meta:
        model = EspeciesPet
        fields= '__all__'

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )
    class Meta:
        model = Petshop
        fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'

class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class EspeciesModelSerializer(ModelSerializer):
    RACA = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:especie-detail'
    )
    class Meta:
        model = EspeciesPet
        fields = '__all__'

class EspecieNestedModelSerializer(ModelSerializer):
    class Meta:
        model = EspeciesPet
        fields = '__all__'

class EspeciesPetRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = EspecieNestedModelSerializer
        super().__init__(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False)
    especie = EspeciesPetRelatedFieldCustomSerializer(
        queryset=EspeciesPet.objects.all(),
        read_only=False
    )

    def validate_data(self, value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Impossível agendar no passado')
    class Meta:
        model = Reserva
        fields = '__all__'

########
class ListaEspeciePetSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nome_pet']