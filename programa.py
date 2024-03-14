from tienda import Restaurante, Tienda, Producto


def main():
    print("Bienvenido al sistema de gestión de tiendas")

    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    tienda = Restaurante(nombre_tienda, costo_delivery)

    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("Opción seleccionada: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto: "))

            tienda.ingresar_producto(nombre_producto, precio_producto, stock_producto)
            print("Producto ingresado con éxito.")

        elif opcion == "2":
            print("Listado de productos:")
            print(tienda.listar_productos())

        elif opcion == "3":
            # Lógica para realizar venta
            pass

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()