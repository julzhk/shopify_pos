from django.test import TestCase

from inventory.models import Inventory

class TestInventory(TestCase):
    def test_createInventory(self):
        i = Inventory.objects.create(title='first_test')
        i.save()
        self.assertTrue(Inventory.objects.count(),1)

    def test_populate_models(self):
        Inventory.populate()
        self.assertTrue(Inventory.objects.count(),2)

    def test_populate_stock(self):
        Inventory().populate_stock()