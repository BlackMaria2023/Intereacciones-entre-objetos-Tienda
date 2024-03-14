class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def aumentar_stock(self, cantidad):
        self.__stock += cantidad
        if self.__stock < 0:
            self.__stock = 0

    def __repr__(self):
        return f"{self.__nombre} - Precio: ${self.__precio} - Stock: {self.__stock}"
    
    
    

