from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @property
    def productos(self):
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock=0):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def ingresar_producto(self, nombre, precio, stock=0):
        producto_existente = next((p for p in self.productos if p.nombre == nombre), None)
        if producto_existente:
            producto_existente.aumentar_stock(stock)
        else:
            self.productos.append(Producto(nombre, precio, 0))  # Siempre stock 0 para restaurantes

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - Precio: ${p.precio}" for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass  # No se realizan ventas en restaurantes

class Supermercado(Tienda):
    def ingresar_producto(self, nombre, precio, stock=0):
        producto_existente = next((p for p in self.productos if p.nombre == nombre), None)
        if producto_existente:
            producto_existente.aumentar_stock(stock)
        else:
            self.productos.append(Producto(nombre, precio, stock))

    def listar_productos(self):
        lista_productos = []
        for producto in self.productos:
            if producto.stock < 10:
                lista_productos.append(f"{producto.nombre} - Precio: ${producto.precio} - Pocos productos disponibles: {producto.stock}")
            else:
                lista_productos.append(f"{producto.nombre} - Precio: ${producto.precio} - Stock: {producto.stock}")
        return "\n".join(lista_productos)

    def realizar_venta(self, nombre_producto, cantidad):
        producto_a_vender = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto_a_vender and producto_a_vender.stock >= cantidad:
            producto_a_vender.aumentar_stock(-cantidad)
            return f"Venta realizada: {cantidad} {nombre_producto}"
        else:
            return "Producto no disponible en stock o cantidad insuficiente"

class Farmacia(Tienda):
    def ingresar_producto(self, nombre, precio, stock=0):
        producto_existente = next((p for p in self.productos if p.nombre == nombre), None)
        if producto_existente:
            producto_existente.aumentar_stock(stock)
        else:
            self.productos.append(Producto(nombre, precio, stock))

    def listar_productos(self):
        lista_productos = []
        for producto in self.productos:
            if producto.precio > 15000:
                lista_productos.append(f"{producto.nombre} - Precio: ${producto.precio} - Envío gratis al solicitar este producto")
            else:
                lista_productos.append(f"{producto.nombre} - Precio: ${producto.precio}")
        return "\n".join(lista_productos)

    def realizar_venta(self, nombre_producto, cantidad):
        producto_a_vender = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto_a_vender and cantidad <= 3 and producto_a_vender.stock >= cantidad:
            producto_a_vender.aumentar_stock(-cantidad)
            return f"Venta realizada: {cantidad} {nombre_producto}"
        elif cantidad > 3:
            return "La cantidad solicitada excede el límite de 3 productos por venta"
        elif producto_a_vender and cantidad > producto_a_vender.stock:
            cantidad_disponible = producto_a_vender.stock
            producto_a_vender.aumentar_stock(-cantidad_disponible)
            return f"Venta realizada: {cantidad_disponible} {nombre_producto}. Stock insuficiente, se vendieron todos los disponibles."
        else:
            return "Producto no disponible en stock o cantidad insuficiente"