

"""
model to store data
"""

import datetime

from flask import jsonify, request
PRODUCTS = list()


class Product:

    def __init__(self, name=None, brand=None, price=None, quantity=None):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.product_id = ''
        self.date = datetime.datetime.now()
    def add_product(self):
        if PRODUCTS == []:
            self.product_id = 0
        else:
            self.product_id = PRODUCTS[-1]['product_id'] + 1

        new_product = {


            "product_id": self.product_id,
            "product_name": self.name,
            "product_brand": self.brand,
            "product_price": self.price,
            "product_quantity": self.quantity
        }
        
        PRODUCTS.append(new_product)
        return new_product
'''
class SaleOrder:
    SALE_ORDER = []
    

    def __init__(self,sale_id=None, name=None, brand=None, price=None, quantity=None):
        self.sale_id = ''
        self.product_id = None
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.date = datetime.datetime.now()
        
    def add_saleOrder(self):
        if SALE_ORDER == []:
            self.sale_id = 0
        else:
            return self.sale_id = SALE_ORDER[-1]['sale_id'] +1
        
        new_sale = {

            "sale_id": self.sale_id,
            "product_id": self.product_id,
            "product_name": self.name,
            "product_brand": self.brand,
            "product_price": self.price,
            "product_quantity": self.quantity
        }
        SALE_ORDER.append(new_sale)
        return new_sale

    def get_sales(self):
        return SALE_ORDER

    def get_single_sale(self, sale_id):
        for sale in SALE_ORDER:
            if sale['sale_id'] == sale_id:
                response_object = {
                    'status': 'success',
                    'data': sale
                }
                return jsonify(response_object), 200 

''' 



