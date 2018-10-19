
from flask import request, jsonify
from flask.views import MethodView
from api.models.product_model import Product


class ProductController(MethodView):
    name = None
    brand = None
    price = None
    quantity = None
    product_data = Product()

    def post(self):
        #post_data = request.get.json()

        product_added = self.product_data.add_product(self.name,self.brand,self.price,self.quantity)

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





    
