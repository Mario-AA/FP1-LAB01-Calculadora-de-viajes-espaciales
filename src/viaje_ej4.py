distancia = 225000000
for vel in range(10000,50001,10000):
    dias = distancia/vel/24
    print(f"Velocidad: {vel} km/h -> Tiempo: {dias} días")