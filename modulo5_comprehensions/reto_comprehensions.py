productos = [
    {
        "nombre": "Laptop",
        "precio": 2500,
        "unidades": 5,
        "categoria": "Tecnología"
    },
    {
        "nombre": "Mouse",
        "precio": 40,
        "unidades": 30,
        "categoria": "Accesorios"
    },
    {
        "nombre": "Teclado",
        "precio": 80,
        "unidades": 15,
        "categoria": "Accesorios"
    },
    {
        "nombre": "Monitor",
        "precio": 900,
        "unidades": 8,
        "categoria": "Tecnología"
    }
]

# 1
valor_total = [
    producto["precio"] * producto["unidades"]
    for producto in productos
]

print("Valor total:")
print(valor_total)

# 2
productos_mayores_1000 = [
    producto["nombre"]
    for producto in productos
    if producto["precio"] * producto["unidades"] > 1000
]

print("\nProductos mayores a 1000:")
print(productos_mayores_1000)

# 3
producto_info = {
    producto["nombre"]: {
        "valor": producto["precio"] * producto["unidades"],
        "unidades": producto["unidades"]
    }
    for producto in productos
}

print("\nInformación:")
print(producto_info)

# 4
ranking_premium = {
    producto["nombre"]:
    producto["precio"] * producto["unidades"]
    for producto in sorted(
        productos,
        key=lambda p: p["precio"] * p["unidades"],
        reverse=True
    )
    if producto["precio"] > 50
}

print("\nRanking premium:")
print(ranking_premium)

# 5
categorias_unicas = {
    producto["categoria"]
    for producto in productos
}

productos_baratos = {
    producto["nombre"]
    for producto in productos
    if producto["precio"] <= 50
}

print("\nCategorías:")
print(categorias_unicas)

print("\nProductos baratos:")
print(productos_baratos)

# 6
resumen_formateado = [
    f"{producto['nombre']} - ${producto['precio']} - {producto['unidades']} unidades"
    for producto in productos
]

gran_total = sum(
    producto["precio"] * producto["unidades"]
    for producto in productos
)

print("\nResumen:")
for item in resumen_formateado:
    print(item)

print("\nGran total:", gran_total)