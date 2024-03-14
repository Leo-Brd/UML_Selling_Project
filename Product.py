# Fichier Product

class Product:
    
    def __init__(self, productId : int, category : str, description : str, productType : str, \
        brand : str, name : str, caracteristics : str, price : float, stock : int) -> None :

        self.__productId = productId
        self.__category = category
        self.__productType = productType
        self.__brand = brand
        self.__name = name
        self.__caracteristics = caracteristics
        self.__description = description
        self.__price = price
        self.__stock = stock
        
    def getProductId(self) -> int:
        return self.__productId
    
    def getCategory(self) -> str:
        return self.__category

    def getProductType(self) -> str:
        return self.__productType
    
    def getBrand(self) -> str:
        return self.__brand
    
    def getName(self) -> str:
        return self.__name
    
    def getCaracteristics(self) -> str:
        return self.__caracteristics
    
    def getDescription(self) -> str:
        return self.__description
    
    def getPrice(self) -> float:
        return self.__price
    
    def getStock(self) -> int:
        return self.__stock
    
    def setProductId(self, productId : int) -> None:
        self.__productId = productId
        
    def setCategory(self, category : str) -> None:
        self.__category = category
    
    def setProductType(self, productType : str) -> None:
        self.__productType = productType
    
    def setBrand(self, brand : str) -> None:
        self.__brand = brand
    
    def setName(self, name : str) -> None:
        self.__name = name
    
    def setCaracteristics(self, caracteristics : str) -> None:
        self.__caracteristics = caracteristics
    
    def setDescription(self, description : str) -> None:
        self.__description = description
    
    def setPrice(self, price : float) -> None:
        self.__price = price
    
    def setStock(self, stock : int) -> None:
        self.__stock = stock
    
    def __str__(self) -> str:
        return f"Product : {self.__name}, {self.__brand}, {self.__productType}, {self.__category}, {self.__description}, {self.__caracteristics}, {self.__price}, {self.__stock}"
    