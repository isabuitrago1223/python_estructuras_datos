catalogo = (
    ("Interestelar", "Christopher Nolan", 2014, 9.0),
    ("Titanic", "James Cameron", 1997, 8.5),
    ("Avatar", "James Cameron", 2009, 8.8),
    ("Inception", "Christopher Nolan", 2010, 9.2)
)

print("=== CATÁLOGO ===")

for titulo, director, año, puntuacion in catalogo:
    print(f"{titulo} | {director} | {año} | {puntuacion}")

# Separar primera película del resto
primera, *resto = catalogo

print("\nPrimera película:")
print(primera)

print("\nResto:")
print(resto)


def buscar_por_director(nombre_director):
    return tuple(
        pelicula
        for pelicula in catalogo
        if pelicula[1] == nombre_director
    )


def obtener_estadisticas():
    puntuaciones = [pelicula[3] for pelicula in catalogo]

    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)

    return minimo, maximo, promedio


print("\nPelículas de James Cameron:")
print(buscar_por_director("James Cameron"))

minimo, maximo, promedio = obtener_estadisticas()

print("\nEstadísticas")
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Promedio:", round(promedio, 2))