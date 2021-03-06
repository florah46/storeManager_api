import unittest
from flask import json
from ..api.app import app
from ..api.vr_1.product_models import Product
from .test_data import NEW_PRODUCT


class TestStoreManager(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)

    def test_add_product(self):
        json_data = json.dumps(NEW_PRODUCT)
        post_data = self.client.post(
            '/api/v1/products/',
            data = json_data,
            content_type='application/json'
        )
        self.assertEqual(post_data.status_code, 201)
    def test_get_product(self):
        post_data = self.client.get(
            '/api/v1/products/',
            content_type='application/json'
        )
        self.assertEqual(post_data.status_code, 200)

        
    #     self.assertTrue(post_response['data'])
    #     self.assertTrue(content_type, 'application/json')
    #     self.assertEqual(status_code, 201)

       

if __name__ == '__main__':
    unittest.main()