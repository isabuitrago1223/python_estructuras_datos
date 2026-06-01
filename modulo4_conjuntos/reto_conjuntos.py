tienda_centro = {
    "Laptop",
    "Mouse",
    "Teclado",
    "Monitor"
}

tienda_norte = {
    "Laptop",
    "Impresora",
    "Monitor"
}

tienda_sur = {
    "Mouse",
    "Teclado",
    "Parlantes"
}

catalogo_completo = (
    tienda_centro.union(tienda_norte)
    .union(tienda_sur)
)

productos_comunes = (
    tienda_centro.intersection(tienda_norte)
)

print("Catálogo completo:")
print(catalogo_completo)

print("\nProductos comunes:")
print(productos_comunes)

print("\nExclusivos Centro:")
print(tienda_centro.difference(tienda_norte))

print("\n¿Norte y Sur son independientes?")
print(tienda_norte.isdisjoint(tienda_sur))

usuario1 = {
    "Acción",
    "Comedia",
    "Drama"
}

usuario2 = {
    "Acción",
    "Terror",
    "Drama"
}

usuario3 = {
    "Comedia",
    "Romance"
}

print("\n=== GÉNEROS ===")

print("Comunes:")
print(usuario1 & usuario2)

print("\nUniverso:")
print(usuario1 | usuario2 | usuario3)

print("\nExclusivos usuario1:")
print(usuario1 - usuario2)

print("\nDiferencia simétrica:")
print(usuario1 ^ usuario2)

print("\n¿Comunes es subconjunto de usuario1?")
print((usuario1 & usuario2) <= usuario1)