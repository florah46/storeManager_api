from .product_controller import ProductController, HomeController



class Routes:
    """
    class for endpoints
    """
    @staticmethod
    def create(app):

        """
        Create urls
        :param app:
        :return:
        """
    
        app.add_url_rule('/', view_func=HomeController.as_view('Home'),
                        methods=["POST"], strict_slashes=False)
        app.add_url_rule('/api/v1/products/', view_func=ProductController.as_view('add_product'),
                        methods=["POST"], strict_slashes=False)
                        
        app.add_url_rule('/api/v1/products', view_func=ProductController.as_view('get_products'),
                        methods=["GET"], strict_slashes=False, defaults={'product_id': None})

        app.add_url_rule('/api/v1/products/<int:product_id>', view_func=ProductController.as_view('get_single_product'),
                        methods=["GET"], strict_slashes=False)                
        

        # app.add_url_rule('/api/v1/sales/', view_func=SaleOrderController.as_view('add_saleOrder'),
        #                 methods=["POST"], strict_slashes=False)
        
        # app.add_url_rule('/api/v1/sales/', view_func=SaleOrderController.as_view('get_sales'),
        #                 methods=["GET"], strict_slashes=False)
    
        # app.add_url_rule('/api/v1/sales/<int:seller>', view_func=SaleOrderController.as_view('get_single_sale'),
        #                 methods=["GET"], strict_slashes=False)                       
               