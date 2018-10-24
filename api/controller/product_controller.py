from flask import request, jsonify
from flask.views import MethodView
from api.models.product_models import Product
from api.models.product_models import SaleOrder




class ProductController(MethodView):
    name = "name"
    brand = "brand"
    price = "price"
    quantity = "quantity"
    product_id = "product_id"
    product_data = Product()

    def post(self):
        #post_data = request.get.json()

        product_added = self.product_data.add_product(self.name,self.brand,self.price,self.quantity,self.product_id)

        response_object = {
            'status': 'Successful',
            'message': 'product added',
            'data': product_added
        }
        return jsonify(response_object), 201

        
    def get(self,product_id=None):
        if product_id:
            return self.get_single(product_id)
        else:
            all_products = self.product_data.get_products()
            response_object = {
                'message': 'Success',
                'data': all_products
            } 
            return jsonify(response_object), 200  

    def get_single(self,product_id):
        for item in self.product_data.get_products():
            if item['product_id'] == product_id:

                response_object = {
                    'message': 'Product got',
                    'data': item
                }
                return jsonify(response_object), 200    



class SaleOrderController(MethodView):
    seller = None
    name = None
    brand = None
    price = None
    quantity = None
    sale_data = SaleOrder()

    def post(self):

        #post_data = request.get.json()

        sale_added = self.sale_data.add_saleOrder(self.seller,self.name,self.brand,self.price,self.quantity)

        response_object = {
            'status': 'Successful',
            'message': 'product added',
            'data': sale_added
        }
        return jsonify(response_object), 201   


    def get(self,seller=None):
        if seller:
            return self.get_single(seller)
        else:
            all_sellers = self.sale_data.get_sales()
            response_object = {
                'message': 'Success',
                'data': all_sellers
            } 
            return jsonify(response_object), 200  


def get_single(self,seller):
        for sale in self.sale_data.get_sales():
            if sale['seller'] == seller:
                response_object = {
                    'message': 'Product got',
                    'data': sale
                }
                return jsonify(response_object), 200
