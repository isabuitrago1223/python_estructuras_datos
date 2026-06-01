ventas_por_region = {
    "Norte": {"Q1": 10000, "Q2": 12000, "Q3": 15000, "Q4": 18000},
    "Sur": {"Q1": 9000, "Q2": 11000, "Q3": 14000, "Q4": 17000},
    "Centro": {"Q1": 13000, "Q2": 14000, "Q3": 16000, "Q4": 20000}
}

print("=== TOTALES ANUALES ===")

totales = {}

for region, ventas in ventas_por_region.items():
    total = sum(ventas.values())
    totales[region] = total
    print(region, ":", total)

mejor_region = max(
    totales,
    key=lambda region: totales[region]
)

print("\nRegión con mayores ventas:")
print(mejor_region)

ventas_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

for region, ventas in ventas_por_region.items():
    for trimestre, valor in ventas.items():
        ventas_trimestre[trimestre] += valor

print("\nVentas por trimestre:")
print(ventas_trimestre)

gran_total = sum(totales.values())

porcentajes = {
    region: round((total / gran_total) * 100, 2)
    for region, total in totales.items()
}

print("\nPorcentajes:")
print(porcentajes)

print("\n=== REPORTE ORDENADO ===")

for region, total in sorted(
        totales.items(),
        key=lambda x: x[1],
        reverse=True):
    print(f"{region}: ${total}")