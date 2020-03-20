import os

import requests
from django.db import models
from django.utils.html import mark_safe

API_KEY, PASSWORD, API_VERSION, SHARED_SECRET = os.environ.get('SHOPIFY_API_KEY'), os.environ.get('PASSWORD'), os.environ.get('API_VERSION'), os.environ.get('SHARED_SECRET')
SHOP_NAME = os.environ.get('SHOP_NAME')
scopes = ','.join(['read_products', 'read_orders'])

shop_url = f"https://%s:%s@{SHOP_NAME}.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, API_VERSION)


class Variant(models.Model):
    variant_id = models.IntegerField(blank=True)
    inventory_item_id = models.TextField(max_length=32, blank=True,default='')
    inventory_quantity = models.IntegerField(blank=True)
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)


class Inventory(models.Model):
    title = models.TextField(max_length=256, blank=True)
    body_html = models.TextField(blank=True)
    available = models.IntegerField(default=0)
    image = models.URLField(blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image}" width="150" height="150" />')

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def populate(cls):
        Inventory.objects.all().delete()
        resource = 'products'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json'
        r = requests.get(auth_url)
        for product_data in r.json()['products']:
            print(product_data)
            product = Inventory.objects.create(title=product_data['title'],
                                               body_html=product_data['body_html'],
                                               image=product_data['images'][0]['src']
                                               )
            for variant in product_data['variants']:
                Variant.objects.create(
                    variant_id=variant['id'],
                    inventory_item_id=variant['inventory_item_id'],
                    inventory_quantity=variant['inventory_quantity'],
                    inventory=product
                ).save()

    @classmethod
    def get_locations(cls):
        resource = 'locations'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json'
        r = requests.get(auth_url)
        locations = [str(item['id']) for item in r.json()['locations']]
        return locations

    @classmethod
    def populate_stock(cls):
        resource = 'inventory_levels'
        locations = ','.join(cls.get_locations())
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json?location_ids={locations}'
        r = requests.get(auth_url)
        data = r.json()
        stock_lookup = {item['inventory_item_id']: item['available'] for item in data['inventory_levels']}
        for stock_id in stock_lookup:
            product = Inventory.objects.get(inventory_item_id=str(stock_id))
            product.objects.update(available=stock_lookup[stock_id])
