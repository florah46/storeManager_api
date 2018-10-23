import unittest
from run import app


class TestProduct(unittest.TestCase):
    def test_add_product(self):
        self.assertEquals(Product,('Iphone7','phone','$450','12','1'))


if __name__ == '__main__':
    unittest.main()
