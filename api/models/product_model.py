"""
model to store data
"""

import datetime

from flask import jsonify


class Home:
    @staticmethod
    def homePage():
        return ("Welcome to Store Manager"), 200

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

    def get_sales(self):
        return self.SaleOrder

    def get_single_sale(self, seller):
        for sale in self.SaleOrder:
            if sale['seller'] == seller:
                response_object = {
                    'status': 'success',
                    'data': sale
                }
                return jsonify(response_object), 200

    SaleOrder = []







    