# Inventario: [nombre, cantidad, precio]

inventario = [
    ["Laptop", 10, 2500],
    ["Mouse", 30, 80],
    ["Teclado", 20, 120]
]


def actualizar_precio(nombre, nuevo_precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[2] = nuevo_precio
            print(f"Precio actualizado para {nombre}")


def registrar_venta(nombre, cantidad):
    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad:
                producto[1] -= cantidad
                print(f"Venta realizada: {cantidad} unidades de {nombre}")
            else:
                print("Stock insuficiente")
            return


def añadir_producto(nombre, cantidad, precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print(f"Stock actualizado para {nombre}")
            return

    inventario.append([nombre, cantidad, precio])
    print(f"Producto {nombre} añadido al inventario")


def mostrar_inventario():
    print("\n===== INVENTARIO =====")
    for nombre, cantidad, precio in inventario:
        print(f"Producto: {nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: ${precio}")
        print("-" * 20)


# Pruebas
actualizar_precio("Mouse", 90)
registrar_venta("Laptop", 2)
añadir_producto("Monitor", 5, 800)

mostrar_inventario()