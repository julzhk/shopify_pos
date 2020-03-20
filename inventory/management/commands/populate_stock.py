from django.core.management.base import BaseCommand, CommandError
from inventory.models import Inventory

class Command(BaseCommand):
    help = 'Populate Stock Available levels'


    def handle(self, *args, **options):
        Inventory.populate_stock()
        self.stdout.write(self.style.SUCCESS('Successfully populated DB with stock'))
