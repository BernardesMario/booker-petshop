from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva no passado!')
        return data
    
    def clean_turno(self):
        turno = self.cleaned_data['turno']
        data = self.cleaned_data['data']
        count = Reserva.objects.filter(data=data, turno=turno).count()
        if count >= 4:
            raise forms.ValidationError('Não é possível agendar nesta data e/ou turno!')
        return turno
    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho','especie', 'petshop', 'observacoes'
    ]