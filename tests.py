import os
import pprint
from unittest import TestCase

import requests
import shopify

API_KEY, PASSWORD, API_VERSION, SHARED_SECRET = os.environ.get('SHOPIFY_API_KEY'), os.environ.get('PASSWORD'), os.environ.get('API_VERSION'), os.environ.get('SHARED_SECRET')
SHOP_NAME = os.environ['SHOP_NAME']
scopes = ','.join(['read_products', 'read_orders'])

shop_url = f"https://%s:%s@{SHOP_NAME}.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, API_VERSION)


class TestAPI(TestCase):
    def test_get_shopify_api(self):
        with shopify.Session.temp(shop_url, 'unstable', 'any-token'):
            assigned_site = shopify.ShopifyResource.site
            print(assigned_site)

    def test_get_products(self):
        resource = 'products'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json'
        r = requests.get(auth_url)
        self.assertEqual(r.status_code, 200)
        data = r.json()['products']
        pprint.pprint(r.json())
        self.assertTrue('OnePlus' in str(data))

    def test_get_location(self):
        resource = 'locations'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json'
        r = requests.get(auth_url)
        self.assertEqual(r.status_code, 200)
        location = r.json()['locations'][0]['id']
        self.assertEqual(location, 14255489091)

    def test_get_inventory(self):
        resource = 'inventory_levels'
        auth_url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/{resource}.json?location_ids=14255489091'
        r = requests.get(auth_url)
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertEqual(len(data['inventory_levels']), 2)


{'inventory_levels': [
    {'admin_graphql_api_id': 'gid://shopify/InventoryLevel/13871349827?inventory_item_id=33032334901315',
     'available': 90,
     'inventory_item_id': 33032334901315,
     'location_id': 14255489091,
     'updated_at': '2020-02-27T14:23:45-05:00'},
    {'admin_graphql_api_id': 'gid://shopify/InventoryLevel/13871349827?inventory_item_id=33032802566211',
     'available': 17,
     'inventory_item_id': 33032802566211,
     'location_id': 14255489091,
     'updated_at': '2020-02-27T14:24:40-05:00'}]}
