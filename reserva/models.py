from django.db import models

# Create your models here.
class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande'),
    )
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='e-mail')
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='dd/mm/aaaa')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=(TURNO_OPCOES))
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    especie = models.ForeignKey(
        'EspeciesPet', 
        related_name='RACA',
        on_delete=models.CASCADE
        )
    observacoes = models.TextField(verbose_name= 'Observações', blank=True, null= True)
    petshop = models.ForeignKey(
        'Petshop', 
        related_name='reservas',
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
    class Meta:
        verbose_name = 'Reserva de banho'
        verbose_name_plural = 'Reservas de banho'

class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)

    def __str__(self):
        return f'{self.nome}, {self.rua}, bairro {self.bairro}'
    class Meta:
        verbose_name = 'Petshop'
        verbose_name_plural = 'Petshops'

class EspeciesPet(models.Model):
    especie = models.CharField(verbose_name='Espécie', max_length=50)

    def __str__(self):
        return self.especie
    
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'