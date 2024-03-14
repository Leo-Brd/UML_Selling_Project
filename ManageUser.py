from User import User
from BuyClasses import Cart, Rental, Product
from Product import Product

class Manage:
    def __init__(self, user: User, cart: Cart, rental: Rental):
        self.user = user
        self.cart = cart
        self.rental = rental

    def add_to_cart(self, product: Product, quantity: int):
        self.cart.addProduct(product.getProductId(), quantity, product.getPrice())

    def add_new_rental(self, product: Product, time_left: int):
        self.rental.addRental(self.user.get_userId(), product.getProductId(), time_left)

    def delete_rental(self, product: Product):
        self.rental.removeRental(self.user.get_userId(), product.getProductId())

    def modif_profile(self, firstName: str, name: str, age: int, email: str, username: str, password: str):
        self.user.set_firstName(firstName)
        self.user.set_name(name)
        self.user.set_age(age)
        self.user.set_email(email)
        self.user.set_username(username)
        self.user.set_password(password)