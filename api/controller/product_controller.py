from flask import request, jsonify
from flask.views import MethodView
from api.models.product_models import Product




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

    