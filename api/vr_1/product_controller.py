from flask import request, jsonify
from flask.views import MethodView
from .product_models import PRODUCTS, Product

class HomeController(MethodView):
    def post(self):
       
        return "Welcome to Store Manager"


class ProductController(MethodView):

    def post(self):
        post_data = request.get_json()

        new_product = Product(post_data['name'], post_data['brand'], post_data['price'], post_data['quantity'])

        response_object = {
            'status': 'Successful',
            'message': 'product added',
            'data': new_product.add_product()
        }
        return jsonify(response_object), 201

        
    def get(self, product_id):
        if product_id is None:
            all_products = list()
            for prod in PRODUCTS:
                all_products.append(prod)
            response_object = {
                    'message': 'Success',
                    'data': all_products
                } 
            return jsonify(response_object), 200
        else:
            for item in PRODUCTS:
                if item['product_id'] == product_id:

                    response_object = {
                        'message': 'Product got',
                        'data': item
                    }
            return jsonify(response_object), 200    


'''
class SaleOrderController(MethodView):
    

    def post(self):

        #post_data = request.get_json()

        sale_added = SaleOrder(post_data[sale_id],post_data['name'],post_data['brand'],post_data['price'],post_data['quantity'])

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
'''