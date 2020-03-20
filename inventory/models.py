from django.db import models
import os
import pprint
from unittest import TestCase
from django.utils.html import mark_safe

import requests
import shopify

API_KEY, PASSWORD, API_VERSION, SHARED_SECRET = os.environ.get('SHOPIFY_API_KEY'), os.environ.get('PASSWORD'), os.environ.get('API_VERSION'), os.environ.get('SHARED_SECRET')
SHOP_NAME = os.environ.get('SHOP_NAME')
scopes = ','.join(['read_products', 'read_orders'])

shop_url = f"https://%s:%s@{SHOP_NAME}.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, API_VERSION)


class Inventory(models.Model):
    title = models.TextField(max_length=256, blank=True)
    body_html = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image}" width="150" height="150" />')

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def populate(cls):
        resource = 'products'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json'
        r = requests.get(auth_url)
        for product_data in r.json()['products']:
            print(product_data)
            product = Inventory(
                title=product_data['title'],
                body_html=product_data['body_html'],
                image = product_data['images'][0]['src']
            ).save()






