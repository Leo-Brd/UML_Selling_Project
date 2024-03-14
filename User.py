# Fichier User

class User:

    def __init__(self, userId: int, firstName: str, name: str, age: int, email: str, username: str, password: str) -> None:
        self.__userId = userId
        self.__firstName = firstName
        self.__name = name
        self.__age = age
        self.__email = email
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return f"User : {self.__userId}, {self.__firstName} {self.__name} {self.__age} {self.__email} {self.__username} {self.__password}"
    
    def get_profil(self):
        return [self.__firstName, self.__name, self.__age, self.__email, self.__username ]

    def get_userId(self):
        return self.__userId

    def get_firstName(self):
        return self.__firstName   
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_email(self):
        return self.__email
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    

    def set_userId(self, userId):
        self.__userId = userId

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password



