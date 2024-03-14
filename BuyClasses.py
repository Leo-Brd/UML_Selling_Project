# Fichier Rental - Cart - Payments

from User import User

class Rental:
    def __init__(self):
        self.__rentalList = [] # Liste des locations (userId, [(productId, time_left), (productId, time_left), ...])
    
    def addRental(self, userId : int, productId : int, time_left : int) -> None:
        if userId in [rental[0] for rental in self.__rentalList]:
            for rental in self.__rentalList:
                if rental[0] == userId:
                    rental[1].append((productId, date))
        else:
            self.__rentalList.append((userId, [(productId, date)]))
            
    def removeRental(self, userId : int, productId : int) -> None:
        for rental in self.__rentalList:
            if rental[0] == userId:
                for product in rental[1]:
                    if product[0] == productId:
                        rental[1].remove(product)
    
    def getRentalList(self) -> list: 
        return self.__rentalList
    
    def getRental(self, userId : int) -> list:
        for rental in self.__rentalList:
            if rental[0] == userId:
                return rental[1]
        return []
    
    def getRentalByProduct(self, productId : int) -> list:
        rentalList = []
        for rental in self.__rentalList:
            for product in rental[1]:
                if product[0] == productId:
                    rentalList.append(rental[0])
        return rentalList
    
    def removeEndedRental(self) -> None:
        for rental in self.__rentalList:
            for product in rental[1]:
                if product[1] <= 0:
                    rental[1].remove(product)


class Cart:
    
    def __init__(self, userId : int) -> None:
        self.__userId = userId
        self.__cartList = []
        self.__totalPrice = 0
    
    def getProductList(self) -> list:
        return self.__cartList
    
    def getTotalPrice(self) -> float:
        return self.__totalPrice
    
    def addProduct(self, productId, quantity, price) -> None:
        self.__cartList.append((productId, quantity, price))
        self.__totalPrice += price * quantity
    
    def removeProduct(self, productId) -> None:
        for product in self.__cartList:
            if product[0] == productId:
                self.__totalPrice -= product[2] * product[1]
                self.__cartList.remove(product)
    
    def emptyCart(self) -> None:
        self.__cartList = []
        self.__totalPrice = 0
    
    def buyCart(self, userId) -> None:
        for product in self.__cartList:
            Payments.payment(userId, self.__totalPrice)
        self.emptyCart()
    
    def __str__(self) -> str:
        return f"Cart : {self.__cartList}, {self.__totalPrice}"
    

class Payments:
    
    def payment(userId : int, price : float) -> None:
        print(f"Payment of, {price}€ for user {userId} done.")
    