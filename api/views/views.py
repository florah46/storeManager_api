from api.controller.product_controller import ProductController


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
    

        app.add_url_rule('/api/v1/products/', view_func=ProductController.as_view('add_product'),
                        methods=["POST"], strict_slashes=False)