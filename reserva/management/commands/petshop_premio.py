#código para criar um sorteio de um cliente(pet) para ganhar um banho gratuito
import random
from django.core.management.base import BaseCommand, CommandParser
from reserva.models import Petshop

class Command(BaseCommand):
    def list_petshops(self):
        return Petshop.objects.all().values_list('pk', flat= True)
    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas podem participar do sorteio?'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help='Digite o ID do petshop que vai realizar o sorteio'
        )

    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        return random.sample(banhos_list, quantidade)


    def imprimir_dados_petshop_sorteio(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Petshop que realizou o sorteio'
            )
        )
        self.stdout.write(f'Loja: {petshop.nome}')

    def imprimir_clientes_sorteados(self, reservas):
        self.stdout.write(
            self.style.HTTP_INFO(
            'Dados dos clientes sorteados'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
            '=' * 35
            )
        )    
        for reserva in reservas:
            self.stdout.write(
                f'Animal: {reserva.nome_pet}'
            )
            self.stdout.write(
                f'Tutor: {reserva.nome} - {reserva.email}'
            )

    def handle(self, *args, **options):
        
        quantity = options['quantity']
        petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()

        banhos_escolhidos =self.escolher_reservas(reservas, quantity)
        
        self.stdout.write(
            self.style.SUCCESS('Sorteio Concluído')
        )
        self.imprimir_dados_petshop_sorteio(petshop)
        self.imprimir_clientes_sorteados(banhos_escolhidos)