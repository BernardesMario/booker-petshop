#código para criar um sorteio de um cliente(pet) para ganhar um banho gratuito

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
    def handle(self, *args, **options):
        pass