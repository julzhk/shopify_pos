from django.test import TestCase

from inventory.models import Inventory

class TestInventory(TestCase):
    def createInventory(self):
        i = Inventory.objects.create(title='first_test')
        i.save()
        self.assertTrue(Inventory.objects.count(),1)