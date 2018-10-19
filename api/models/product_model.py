"""
model to store data
"""

import datetime

from flask import jsonify



class Product:
    increment = 0

    def __init__(self, name=None, brand=None, price=None, quantity=None):
        self.product_id = None
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.date = datetime.datetime.now()
    def add_product(self,name, brand, price, quantity):
        self.increment += 1
        current_product = Product(name,brand,price,quantity)
        current_product.product_id = self.increment
        new_product = {


            "product_id": current_product.product_id,
            "product_name": current_product.name,
            "product_brand": current_product.brand,
            "product_price": current_product.price,
            "product_quantity": current_product.quantity
        }
        self.product.append(new_product)
        return self.product  

    def get_products(self):
        return self.product

    def get_single_product(self, product_id):
        for item in self.product:
            if item['product_id'] == product_id:
                response_object = {
                    'status': 'success',
                    'data': item
                }
                return jsonify(response_object), 200
            
    

    product=[]    


class SaleOrder:

    def __init__(self, name=None, brand=None, price=None, quantity=None):
        self.product_id = None
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.date = datetime.datetime.now()
        
    def add_saleOrder(self,name,brand,price,quantity):
        new_sale = Product(name,brand,price,quantity)
        new_sale.product_id = self.increment
        new_product = {


            "product_id": current_product.product_id,
            "product_name": current_product.name,
            "product_brand": current_product.brand,
            "product_price": current_product.price,
            "product_quantity": current_product.quantity
        }
        self.product.append(new_product)
        return self.product  







    