from django.core.management.base import BaseCommand, CommandError
from inventory.models import Inventory

class Command(BaseCommand):
    help = 'Populate Products'


    def handle(self, *args, **options):
        Inventory.populate()
        self.stdout.write(self.style.SUCCESS('Successfully populated DB'))
