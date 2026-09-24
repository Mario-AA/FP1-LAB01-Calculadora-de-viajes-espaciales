distancia = int(input("Ingrese la distancia total del viaje en km"))
dist_rep = 150000
paradas = 0
for distancia in range (0,distancia,dist_rep):
    print(f"Parada en el km {distancia}")
    paradas +=1
print(f"Total de paradas para respostar: {paradas}")