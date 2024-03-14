# Fichier comprenant un exemple de Test Client 

import unittest
from BuyClasses import Rental, Cart, Payments
from Product import Product
from User import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "John", "Doe", 25, "email", "username", "password")

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.get_userId(), 1)
        self.assertEqual(self.user.get_firstName(), "John")
        self.assertEqual(self.user.get_name(), "Doe")
        self.assertEqual(self.user.get_age(), 25)
        self.assertEqual(self.user.get_email(), "email")
        self.assertEqual(self.user.get_username(), "username")
        self.assertEqual(self.user.get_password(), "password")

class TestRental(unittest.TestCase):
    def setUp(self):
        self.rental = Rental()

    def test_rental_creation(self):
        self.assertIsInstance(self.rental, Rental)

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart(1)

    def test_cart_creation(self):
        self.assertEqual(self.cart.getProductList(), [])
        self.assertEqual(self.cart.getTotalPrice(), 0)

class TestPayments(unittest.TestCase):
    def setUp(self):
        self.payments = Payments()

    def test_payments_creation(self):
        self.assertIsInstance(self.payments, Payments)

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "category", "description", "productType", "brand", "name", "caracteristics", 2, 5)

    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.getProductId(), 1)
        self.assertEqual(self.product.getCategory(), "category")
        self.assertEqual(self.product.getDescription(), "description")
        self.assertEqual(self.product.getProductType(), "productType")
        self.assertEqual(self.product.getBrand(), "brand")
        self.assertEqual(self.product.getName(), "name")
        self.assertEqual(self.product.getCaracteristics(), "caracteristics")
        self.assertEqual(self.product.getPrice(), 2)
        self.assertEqual(self.product.getStock(), 5)

if __name__ == '__main__':
    unittest.main()