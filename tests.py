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


'''
{'products': [{'admin_graphql_api_id': 'gid://shopify/Product/4408178344003',
               'body_html': '<meta http-equiv="content-type" '
                            'content="text/html; charset=utf-8">\n'
                            '<ul class="a-unordered-list a-vertical '
                            'a-spacing-none">\n'
                            '<li><span class="a-list-item">Rear Camera; 48MP '
                            '(Primary)+ 8MP (Tele-photo)+16MP (ultrawide); '
                            'Front Camera;16 MP POP-UP Camera; You will need '
                            'to chargethe phone when you first get it or if '
                            'you have not used it for a long time</span></li>\n'
                            '<li><span class="a-list-item">16.9 centimeters '
                            '(6.67-inch) multi-touch capacitive touchscreen '
                            'with 3120 x 1440 pixels resolution</span></li>\n'
                            '<li><span class="a-list-item">Memory, Storage and '
                            'SIM: 8GB RAM | 256GB internal memory | Dual SIM '
                            'dual-standby (4G+4G)</span></li>\n'
                            '<li><span class="a-list-item">Android Oxygen '
                            'operating system with 2.84GHz Snapdragon 855 octa '
                            'core processor</span></li>\n'
                            '<li><span class="a-list-item">4000mAH lithium-ion '
                            'battery, Buttons: Gestures and on-screen '
                            'navigation support; Alert Slider</span></li>\n'
                            '<li><span class="a-list-item">1 year manufacturer '
                            'warranty for device and 6 months manufacturer '
                            'warranty for in-box accessories including '
                            'batteries from the date of purchase</span></li>\n'
                            '<li><span class="a-list-item">Box also includes: '
                            'Power Adapter, Type-C Cable (Support USB 2.0), '
                            'Quick Start Guide, Welcome Letter, Safety '
                            'Information and Warranty Card, Logo Sticker, '
                            'Case, Screen Protector (pre-applied) and SIM Tray '
                            'Ejector</span></li>\n'
                            '</ul>',
               'created_at': '2020-02-27T12:45:17-05:00',
               'handle': 'copy-of-oneplus-7-pro-nebula-blue-8gb-ram-fluid-amoled-display-256gb-storage-4000mah-battery',
               'id': 4408178344003,
               'image': {'admin_graphql_api_id': 'gid://shopify/ProductImage/13792399360067',
                         'alt': None,
                         'created_at': '2020-02-27T12:45:17-05:00',
                         'height': 1000,
                         'id': 13792399360067,
                         'position': 1,
                         'product_id': 4408178344003,
                         'src': 'https://cdn.shopify.com/s/files/1/0015/4589/6003/products/51FwsSj8knL._SL1000_d02ca740-0556-48c5-bdc3-8f8f2347e72e.jpg?v=1582825517',
                         'updated_at': '2020-02-27T12:45:17-05:00',
                         'variant_ids': [],
                         'width': 1000},
               'images': [{'admin_graphql_api_id': 'gid://shopify/ProductImage/13792399360067',
                           'alt': None,
                           'created_at': '2020-02-27T12:45:17-05:00',
                           'height': 1000,
                           'id': 13792399360067,
                           'position': 1,
                           'product_id': 4408178344003,
                           'src': 'https://cdn.shopify.com/s/files/1/0015/4589/6003/products/51FwsSj8knL._SL1000_d02ca740-0556-48c5-bdc3-8f8f2347e72e.jpg?v=1582825517',
                           'updated_at': '2020-02-27T12:45:17-05:00',
                           'variant_ids': [],
                           'width': 1000}],
               'options': [{'id': 5738220257347,
                            'name': 'Title',
                            'position': 1,
                            'product_id': 4408178344003,
                            'values': ['Default Title']}],
               'product_type': 'product_type',
               'published_at': '2020-02-27T12:45:17-05:00',
               'published_scope': 'global',
               'tags': '',
               'template_suffix': '',
               'title': 'One Plus 100',
               'updated_at': '2020-03-20T05:55:42-04:00',
               'variants': [{'admin_graphql_api_id': 'gid://shopify/ProductVariant/31437245612099',
                             'barcode': 'BARCODE',
                             'compare_at_price': '52999.00',
                             'created_at': '2020-02-27T12:45:17-05:00',
                             'fulfillment_service': 'manual',
                             'grams': 0,
                             'id': 31437245612099,
                             'image_id': None,
                             'inventory_item_id': 33032802566211,
                             'inventory_management': 'shopify',
                             'inventory_policy': 'deny',
                             'inventory_quantity': 17,
                             'old_inventory_quantity': 17,
                             'option1': 'Default Title',
                             'option2': None,
                             'option3': None,
                             'position': 1,
                             'price': '42999.00',
                             'product_id': 4408178344003,
                             'requires_shipping': True,
                             'sku': 'ONEPLUS',
                             'taxable': False,
                             'title': 'Default Title',
                             'updated_at': '2020-02-27T14:24:40-05:00',
                             'weight': 0.0,
                             'weight_unit': 'kg'}],
               'vendor': 'vendor'},
              {'admin_graphql_api_id': 'gid://shopify/Product/4408136663107',
               'body_html': '<meta http-equiv="content-type" '
                            'content="text/html; charset=utf-8">\n'
                            '<ul class="a-unordered-list a-vertical '
                            'a-spacing-none">\n'
                            '<li><span class="a-list-item">Rear Camera; 48MP '
                            '(Primary)+ 8MP (Tele-photo)+16MP (ultrawide); '
                            'Front Camera;16 MP POP-UP Camera; You will need '
                            'to chargethe phone when you first get it or if '
                            'you have not used it for a long time</span></li>\n'
                            '<li><span class="a-list-item">16.9 centimeters '
                            '(6.67-inch) multi-touch capacitive touchscreen '
                            'with 3120 x 1440 pixels resolution</span></li>\n'
                            '<li><span class="a-list-item">Memory, Storage and '
                            'SIM: 8GB RAM | 256GB internal memory | Dual SIM '
                            'dual-standby (4G+4G)</span></li>\n'
                            '<li><span class="a-list-item">Android Oxygen '
                            'operating system with 2.84GHz Snapdragon 855 octa '
                            'core processor</span></li>\n'
                            '<li><span class="a-list-item">4000mAH lithium-ion '
                            'battery, Buttons: Gestures and on-screen '
                            'navigation support; Alert Slider</span></li>\n'
                            '<li><span class="a-list-item">1 year manufacturer '
                            'warranty for device and 6 months manufacturer '
                            'warranty for in-box accessories including '
                            'batteries from the date of purchase</span></li>\n'
                            '<li><span class="a-list-item">Box also includes: '
                            'Power Adapter, Type-C Cable (Support USB 2.0), '
                            'Quick Start Guide, Welcome Letter, Safety '
                            'Information and Warranty Card, Logo Sticker, '
                            'Case, Screen Protector (pre-applied) and SIM Tray '
                            'Ejector</span></li>\n'
                            '</ul>',
               'created_at': '2020-02-27T11:28:22-05:00',
               'handle': 'oneplus-7-pro-nebula-blue-8gb-ram-fluid-amoled-display-256gb-storage-4000mah-battery',
               'id': 4408136663107,
               'image': {'admin_graphql_api_id': 'gid://shopify/ProductImage/13792249544771',
                         'alt': None,
                         'created_at': '2020-02-27T11:28:22-05:00',
                         'height': 1000,
                         'id': 13792249544771,
                         'position': 1,
                         'product_id': 4408136663107,
                         'src': 'https://cdn.shopify.com/s/files/1/0015/4589/6003/products/51FwsSj8knL._SL1000.jpg?v=1582820902',
                         'updated_at': '2020-02-27T11:28:22-05:00',
                         'variant_ids': [],
                         'width': 1000},
               'images': [{'admin_graphql_api_id': 'gid://shopify/ProductImage/13792249544771',
                           'alt': None,
                           'created_at': '2020-02-27T11:28:22-05:00',
                           'height': 1000,
                           'id': 13792249544771,
                           'position': 1,
                           'product_id': 4408136663107,
                           'src': 'https://cdn.shopify.com/s/files/1/0015/4589/6003/products/51FwsSj8knL._SL1000.jpg?v=1582820902',
                           'updated_at': '2020-02-27T11:28:22-05:00',
                           'variant_ids': [],
                           'width': 1000}],
               'options': [{'id': 5738168844355,
                            'name': 'Title',
                            'position': 1,
                            'product_id': 4408136663107,
                            'values': ['Default Title']}],
               'product_type': 'product_type',
               'published_at': '2020-02-27T11:05:14-05:00',
               'published_scope': 'global',
               'tags': '',
               'template_suffix': '',
               'title': 'OnePlus 7 Pro (Nebula Blue, 8GB RAM, Fluid AMOLED '
                        'Display, 256GB Storage, 4000mAH Battery)',
               'updated_at': '2020-03-20T05:55:42-04:00',
               'variants': [{'admin_graphql_api_id': 'gid://shopify/ProductVariant/31436805668931',
                             'barcode': 'BARCODE',
                             'compare_at_price': '52999.00',
                             'created_at': '2020-02-27T11:28:22-05:00',
                             'fulfillment_service': 'manual',
                             'grams': 0,
                             'id': 31436805668931,
                             'image_id': None,
                             'inventory_item_id': 33032334901315,
                             'inventory_management': 'shopify',
                             'inventory_policy': 'deny',
                             'inventory_quantity': 90,
                             'old_inventory_quantity': 90,
                             'option1': 'Default Title',
                             
'option2': None,
                             
'option3': None,
                             Ran 2 tests in 0.391s

OK
'position': 1,
                             'price': '42999.00',
                             'product_id': 4408136663107,
                             'requires_shipping': True,
                             'sku': 'ONEPLUS',
                             'taxable': False,
                             'title': 'Default Title',
                             'updated_at': '2020-02-27T14:23:45-05:00',
                             'weight': 0.0,
                             'weight_unit': 'kg'}],
               'vendor': 'vendor'}]}
https://mishipaytestdevelopmentemptystore.myshopify.com/admin/api/unstable
'''
