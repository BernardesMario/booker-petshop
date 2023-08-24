from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(verbose_name= 'Nome', max_length=50)
    email = models.EmailField(verbose_name= 'Email', max_length=50)
    mensagem = models.TextField(verbose_name= 'Mensagem')
    data = models.DateTimeField(verbose_name= 'Data de Envio',auto_now_add=True)
    lido = models.BooleanField(verbose_name= 'Lido', default= False, blank= True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']