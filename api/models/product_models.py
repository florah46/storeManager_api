

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

    def get_products(self):
        return product


    def get_single_product(self, product_id):
        for item in product:
            if item['product_id'] == product_id:
                response_object = {
                    'status': 'success',
                    'data': item
                }
                return jsonify(response_object), 200          

product=[]


class SaleOrder:
    increament = 0

    def __init__(self,seller=None, name=None, brand=None, price=None, quantity=None):
        self.seller = seller
        self.product_id = None
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.date = datetime.datetime.now()
        
    def add_saleOrder(self,seller,name,brand,price,quantity):
        self.increament += 1
        new_sale = SaleOrder(seller,name,brand,price,quantity)
        new_sale.seller = self.increament
        sale_details = {

            "seller": new_sale.seller,
            "product_id": new_sale.product_id,
            "product_name": new_sale.name,
            "product_brand": new_sale.brand,
            "product_price": new_sale.price,
            "product_quantity": new_sale.quantity
        }
        self.SaleOrder.append(sale_details)
        return self.SaleOrder 




