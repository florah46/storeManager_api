

"""
model to store data
"""

import datetime

from flask import jsonify, request



class Product:


    def __init__(self, name=None, brand=None, price=None, quantity=None, product_id = None):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.product_id = product_id
        self.date = datetime.datetime.now()
    def add_product(self,name, brand, price, quantity,product_id):
        
        new_product = {


            "product_id": product_id,
            "product_name": self.name,
            "product_brand": self.brand,
            "product_price": self.price,
            "product_quantity": self.quantity
        }
        
        product.append(new_product)
        return new_product

        if product is []:
            return product_id is 1
        else:
            return product_id is product[-1]["product_id"]+1



product=[]